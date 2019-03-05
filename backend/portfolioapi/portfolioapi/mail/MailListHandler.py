import json
import html
import os
from email.utils import parseaddr
from threading import Thread

import pymysql
import pymysql.cursors

from flask_mail import Message
from flask import render_template, current_app

from portfolioapi.utils import DbHelper, ResponseHandler, hash_message


class MailListHandler:
	"""
	This class handles all Mail List functionality within my app.
	"""
	def __init__(self, mail, app):
		self.app = app
		self.mail = mail
		self.rh = ResponseHandler()

	@staticmethod
	def validate_email(email):
		"""
		This function returns true if email is well formed before
		sending confirmation email, it returns false if not.
		"""
		temp = email.split("@")

		if len(temp) != 2:
			return False

		if not temp[0] or not temp[1]:
			return False

		if "." not in temp[1]:
			return False

		temp = temp[1].split(".")

		for domain_part in temp:
			if not domain_part:
				return False

		return True

	@staticmethod
	def get_mailing_list():
		"""
		Returns mailing list for all activated members of the mailing list.
		"""
		result = {}
		connection = DbHelper.connect()

		with connection.cursor() as cursor:
			sql = "SELECT email FROM mail_list \
				   WHERE is_activated=1;"
			cursor.execute(sql)
			result = cursor.fetchall()

		return [email_data['email'] for email_data in result]

	# Async function was not working, need to add it back later
	# def send_async_mail(self, msg):
	# 	with self.app.app_context():
	# 		self.mail.send(msg)
	# 		print("Sent.")

	def create_new_sub(self, email_address, email_hash):
		"""
		Creates a new column in the mail_list table database.
		"""
		result = {}
		sub_id = 0
		# connect to DB
		connection = DbHelper.connect()
		try:
			with connection.cursor() as cursor:
				sql = "INSERT INTO mail_list (email, email_hash) \
					   VALUES (%s, %s);"
				cursor.execute(sql, [email_address, email_hash])
				sub_id = cursor.lastrowid
				connection.commit()	
		except pymysql.MySQLError as e:
			connection.close()
			if str(e.args[0]) == "1062":
				return "EMAIL_ALREADY_EXISTS"
			else:
				return "DATABASE_ERROR"
		else:
			with connection.cursor() as cursor:
				# print(sub_id)
				sql = "SELECT email FROM mail_list WHERE sub_id=%s;"
				cursor.execute(sql, [sub_id])
				result = cursor.fetchone()
				connection.close()
			return result

	def send_confirmation_email(self, email_address, email_hash):
		msg = Message(subject="Confirm Subscription to Nigel's Blog",
					  sender="noreply@nigelhaney.me",
					  recipients=[email_address])
		unique_url = "https://nigelhaney.me/api/mail/confirm/" + email_hash

		msg.body=("Confirm subscription to Nigel's blog by visiting " + \
					unique_url)
		msg.html=render_template("confirmationemail.html", 
								activation_url=unique_url)
		self.mail.send(msg)
		return
	
	def confirmation_email_handler(self, data):
		"""
		This will send a confirmation email to the user if the user does not
		already exist in the table and the email is valid.

		It will need to create a row on the mail_list table for the user which
		is currently unactivated. This is done with method create_new_sub().

		It will send a confirmation email out with a link that results to a hash
		of the user's address.

		If the get request is triggered at the link that corresponds to the 
		hashed valueof an address in the table that is both unactivated 
		and present in the table, the email address will be activated and mail 
		will be sent to it.
		"""
		data_obj = json.loads(data)
		status = ""
		email_hash = ""
		
		if "email" not in data_obj:
			return self.rh.response_builder("INVALID_EMAIL")
		else:
			email_address = str(data_obj['email'])

		if not email_address or not MailListHandler.validate_email(email_address):
			status = "INVALID_EMAIL"
		else:
			email_hash = hash_message(email_address)
			status = self.create_new_sub(email_address, email_hash)
			
		return_data = self.rh.response_builder(status)

		if return_data['code'] == 200:
			try:
				self.send_confirmation_email(email_address, email_hash)
			except:
				return self.rh.response_builder("MAIL_SERVER_ERROR")
		
		return return_data

	def confirm_subscription(self, sub_code):
		"""
		This function will check to see if the link a user clicked is
		is valid. If it is they will be activated in the database to
		receive emails. (Their email will be reported by get_mailing_list)
		Things to check for:
		- Doesn't exist
		- Already activated
		- Is unactivated, this means we need to update it.
		"""
		result = {}
		connection = DbHelper.connect()
		sub_id = 0
		# print("Subscription Code: " + sub_code)

		try:
			with connection.cursor() as cursor:
				sql = "SELECT * FROM mail_list \
					   WHERE email_hash=%s;"
				cursor.execute(sql, [sub_code])
				result = cursor.fetchone()
				
				if not result:
					connection.close()
					return "CODE_DOES_NOT_EXIST"
				
				elif result['is_activated']:
					connection.close()
					return "CODE_ALREADY_ACTIVATED"

				sub_id = result['sub_id']

				sql = "UPDATE mail_list \
					   SET is_activated=is_activated+1 \
					   WHERE sub_id=%s;"
				cursor.execute(sql, [sub_id])
				connection.commit()
				connection.close()
				return result
		except pymysql.MySQLError as e:
			connection.close()
			return "DATABASE_ERROR"

	def subscription_confirmation_handler(self, sub_code):
		result = self.rh.response_builder(self.confirm_subscription(sub_code))

		if result['code'] == 200:
			return render_template("confirmationpage.html", success=True,
															message=result['data']['email'],
															code=result['data']['email_hash'])
		else:
			return render_template("confirmationpage.html", success=False,
															message=result['message'])

	def unsubscribe(self, sub_code):
		"""
		This function will unsubscribe the user from the mail_list table
		(deleting them from it)

		Things to check:
		- User is not activated.
		- User does not exist.
		
		This function will just deal with the DB, the handler function
		will be responsible for forming a response.
		"""
		result = {}
		connection = DbHelper.connect()
		sub_id = 0

		try:
			with connection.cursor() as cursor:
				sql = "SELECT * FROM mail_list \
					   WHERE email_hash=%s;"
				cursor.execute(sql, [sub_code])
				result = cursor.fetchone()
				
				if not result:
					connection.close()
					return "CODE_DOES_NOT_EXIST"
				elif not result['is_activated']:
					connection.close()
					return "CODE_NOT_ACTIVATED"

				sub_id = result['sub_id']

				sql = "DELETE FROM mail_list \
					   WHERE sub_id=%s;"
				cursor.execute(sql, [sub_id])
				connection.commit()
				connection.close()
				return "UNSUBSCRIBED"
		except pymysql.MySQLError as e:
			connection.close()
			return "DATABASE_ERROR"

	def unsubscribe_handler(self, sub_code):
		result = self.rh.response_builder(self.unsubscribe(sub_code))

		if result['code'] == 200:
			return render_template("unsubscribepage.html", success=True)
		else:
			return render_template("unsubscribepage.html", success=False,
														   message=result['message'])

	def broadcast_to_users(self, post_title, post_excerpt, post_url):
		email_list = MailListHandler.get_mailing_list()

		with self.mail.connect() as conn:
			for email in email_list:
				msg = Message(subject=post_title,
					  sender="noreplynigelsblog@gmail.com",
					  recipients=[email])
		
				email_hash = hash_message(email)
				msg.body=("Nigel made a new post titled " + post_title + ". " + post_excerpt + \
					"Visit " + post_url + " to read.")
				msg.html=render_template("newblogemail.html", 
										email_hash=email_hash,
										post_title=post_title,
										post_excerpt=post_excerpt,
										blog_url=post_url)

				conn.send(msg)

		return

	def clear_mail_list(self):
		self.connection = DbHelper.connect()
		result = {}

		try:
			with self.connection.cursor() as cursor:
				sql = "DELETE FROM mail_list;"
				cursor.execute(sql)
				self.connection.commit()
		except pymysql.MySQLError as e:
			print(e, e.args)
			self.connection.close()
			return "DATABASE_ERROR"
		else:
			self.connection.close()
			return "POST_DELETED"














