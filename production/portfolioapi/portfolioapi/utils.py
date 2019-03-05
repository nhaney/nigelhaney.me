import hmac
import hashlib
import base64
import os
import json
import pymysql

from flask import current_app

class DbHelper:
	@staticmethod
	def connect():
		if current_app.config['TESTING']:
			db_name = "portfoliosite"
		else:
			db_name = "prod_portfoliosite"

		return pymysql.connect(host='localhost',
							  user=current_app.config['MYSQL_USERNAME'],
							  password=current_app.config['MYSQL_PASSWORD'],
							  db=db_name,
							  cursorclass=pymysql.cursors.DictCursor)


class ResponseHandler:
	"""
	This class is in charge of properly forming a well-structured response from
	the API.
	"""
	def __init__(self):
		self.error_messages = {
			"INVALID_TITLE":(400, "Title of blog post cannot be stored in database."),
			"INVALID_CONTENT":(400, "Content of blog post cannot be stored in database."),
			"UNAUTHORIZED_REQUEST":(401, "Unauthorized request. Use proper authentication header to use this service."),
			"POST_ALREADY_EXISTS":(400, "Cannot create blog post because it already exists."),
			"DATABASE_ERROR":(500, "Internal database error, my service is down."),
			"POST_NOT_FOUND":(404, "Post requested does not exist."),
			"COMMENT_NOT_FOUND":(404, "Comment requested does not exist."),
			"INVALID_AUTHOR":(400, "Invalid name entered."),
			"INVALID_COMMENT_CONTENT":(400, "Invalid comment entered."),
			"INVALID_NAME":(400, "Invalid name entered for leaderboard."),
			"GAME_NOT_FOUND":(400, "Invalid game name entered for leaderboard retrieval"),
			"INVALID_EMAIL":(400, "MInvalid email address entered."),
			"EMAIL_ALREADY_EXISTS":(400, "Email already exists in mailing list."),
			"MAIL_SERVER_ERROR":(500, "Mail server unable to send email."),
			"CODE_DOES_NOT_EXIST":(404, "Email not registered for mailing list."),
			"CODE_ALREADY_ACTIVATED":(400, "This email has already been activated."),
			"CODE_NOT_ACTIVATED":(400, "This email has not yet subscribed."),
			"NO_POSTS_EXIST":(400, "No posts have been made yet, check back later."),
			"":(500, "Table handler failed.")

		}

	def response_builder(self, status):
		response = {}
		if str(status) in self.error_messages:
			# error occurred
			response["status"] = status
			response["code"] = self.error_messages[status][0]
			response["message"] = self.error_messages[status][1]
		else:
			response["status"] = "SUCCESS"
			response["code"] = 200
			response["message"] = "Request sucessfully fulfilled."
			response["data"] = status

		return response


def hash_message(message):
	"""
	This function hashes a message using the secret key
	"""
	
	dig = hmac.new(str.encode(current_app.config['SECRET_KEY']), 
		msg=str.encode(message), 
		digestmod=hashlib.sha256).digest()
	return base64.b64encode(dig).decode()


def make_json_response(data, status_code, data_type='application/json'):
	return current_app.response_class(
		response=json.dumps(data, indent=4, sort_keys=True, default=str),
		status=status_code,
		mimetype=data_type
	)