import unittest
import json
import sys
import os

from flask_mail import Mail
from flask import current_app

sys.path.append("../../portfolioapi")
from portfolioapi.mail.MailListHandler import MailListHandler
from portfolioapi import create_app
from portfolioapi.config import TestConfig
from portfolioapi.utils import hash_message

app = create_app(TestConfig)
mail = Mail(app)


class TestMailListHandler(unittest.TestCase):
	def test_validate_email(self):
		self.assertEqual(False, MailListHandler.validate_email("awefawe"))
		self.assertEqual(True, MailListHandler.validate_email("nigel.haney@gmail.com"))
		self.assertEqual(False, MailListHandler.validate_email("@"))
		self.assertEqual(False, MailListHandler.validate_email("aewf@awefafwe"))
		self.assertEqual(True, MailListHandler.validate_email("awe@awefaew.ceaw"))

	def test_create_new_sub_success(self):
		mail_list_handler = MailListHandler(mail, current_app)
		mail_list_handler.clear_mail_list()

		test_email = "test@test.com"
		test_hash = hash_message(test_email)

		test_result = mail_list_handler.create_new_sub(
						test_email,
						test_hash
					  )

		self.assertEqual(test_result['email'], test_email)
		mail_list_handler.clear_mail_list()
		return

	def test_create_new_sub_duplicate(self):
		mail_list_handler = MailListHandler(mail, current_app)
		mail_list_handler.clear_mail_list()

		test_email = "test@test.com"
		test_hash = hash_message(test_email)

		mail_list_handler.create_new_sub(test_email, test_hash)

		test_result = mail_list_handler.create_new_sub(
						test_email,
						test_hash
					  )

		self.assertEqual(test_result, "EMAIL_ALREADY_EXISTS")
		mail_list_handler.clear_mail_list()
		return

	def test_get_mailing_list(self):
		mail_list_handler = MailListHandler(mail, current_app)
		mail_list_handler.clear_mail_list()

		test_email = "test@test.com"
		test_hash = hash_message(test_email)

		mail_list_handler.create_new_sub(test_email, test_hash)
		mail_list_handler.confirm_subscription(test_hash)

		self.assertEqual(len(MailListHandler.get_mailing_list()), 1)

		test_email = "test1@test.com"
		test_hash = hash_message(test_email)

		mail_list_handler.create_new_sub(test_email, test_hash)
		mail_list_handler.confirm_subscription(test_hash)

		self.assertEqual(len(MailListHandler.get_mailing_list()), 2)

		mail_list_handler.clear_mail_list()
		return

	def test_send_confirmation_email(self):
		mail_list_handler = MailListHandler(mail, current_app)
		mail_list_handler.clear_mail_list()

		test_email = "test@test.com"
		test_hash = hash_message(test_email)

		with mail.record_messages() as outbox:
			mail_list_handler.send_confirmation_email(test_email, test_hash)

			self.assertEqual(len(outbox), 1)
			self.assertEqual(outbox[0].subject, "Confirm Subscription to Nigel's Blog")
			self.assertTrue('test@test.com' in outbox[0].recipients)
		return

	def test_confirmation_email_handler_invalid_email(self):
		mail_list_handler = MailListHandler(mail, current_app)
		mail_list_handler.clear_mail_list()

		test_data = json.dumps({
						"not_email":"nigel@nigel.com"
					})

		test_result = mail_list_handler.confirmation_email_handler(test_data)

		self.assertEqual(test_result['status'], "INVALID_EMAIL")

		test_data = json.dumps({
						"email":""
					})
		
		test_result = mail_list_handler.confirmation_email_handler(test_data)

		self.assertEqual(test_result['status'], "INVALID_EMAIL")

		test_data = json.dumps({
						"email":1
					})
		
		test_result = mail_list_handler.confirmation_email_handler(test_data)

		self.assertEqual(test_result['status'], "INVALID_EMAIL")

		mail_list_handler.clear_mail_list()
		return

	def test_confirmation_email_handler_success(self):
		mail_list_handler = MailListHandler(mail, current_app)
		mail_list_handler.clear_mail_list()

		test_data = json.dumps({
						"email":"nigel@nigel.com"
					})

		with mail.record_messages() as outbox:
			test_result = mail_list_handler.confirmation_email_handler(test_data)

			self.assertEqual(len(outbox), 1)
			self.assertTrue('nigel@nigel.com' in outbox[0].recipients)

		mail_list_handler.clear_mail_list()
		return

	def test_confirm_subscription_does_not_exist(self):
		mail_list_handler = MailListHandler(mail, current_app)
		mail_list_handler.clear_mail_list()

		test_email = "test@test.com"
		test_hash = hash_message(test_email)

		test_result = mail_list_handler.confirm_subscription(test_hash)

		self.assertEqual(test_result, "CODE_DOES_NOT_EXIST")
		
		mail_list_handler.clear_mail_list()
		return

	def test_confirm_subscription_success(self):
		mail_list_handler = MailListHandler(mail, current_app)
		mail_list_handler.clear_mail_list()

		test_email = "test@test.com"
		test_hash = hash_message(test_email)

		mail_list_handler.create_new_sub(test_email, test_hash)

		test_result = mail_list_handler.confirm_subscription(test_hash)

		self.assertEqual(test_result['email'], test_email)

		mail_list_handler.clear_mail_list()
		return

	def test_confirm_subscription_already_activated(self):
		mail_list_handler = MailListHandler(mail, current_app)
		mail_list_handler.clear_mail_list()

		test_email = "test@test.com"
		test_hash = hash_message(test_email)

		mail_list_handler.create_new_sub(test_email, test_hash)

		mail_list_handler.confirm_subscription(test_hash)

		test_result = mail_list_handler.confirm_subscription(test_hash)

		self.assertEqual(test_result, "CODE_ALREADY_ACTIVATED")

		mail_list_handler.clear_mail_list()
		return

	def test_unsubscribe_code_not_found(self):
		mail_list_handler = MailListHandler(mail, current_app)
		mail_list_handler.clear_mail_list()

		test_email = "test@test.com"
		test_hash = hash_message(test_email)

		test_result = mail_list_handler.unsubscribe(test_hash)

		self.assertEqual(test_result, "CODE_DOES_NOT_EXIST")

		mail_list_handler.clear_mail_list()
		return

	def test_unsubscribe_not_activated(self):
		mail_list_handler = MailListHandler(mail, current_app)
		mail_list_handler.clear_mail_list()

		test_email = "test@test.com"
		test_hash = hash_message(test_email)

		mail_list_handler.create_new_sub(test_email, test_hash)

		test_result = mail_list_handler.unsubscribe(test_hash)

		self.assertEqual(test_result, "CODE_NOT_ACTIVATED")

		mail_list_handler.clear_mail_list()
		return

	def test_unsubscribe_success(self):
		mail_list_handler = MailListHandler(mail, current_app)
		mail_list_handler.clear_mail_list()

		test_email = "test@test.com"
		test_hash = hash_message(test_email)

		mail_list_handler.create_new_sub(test_email, test_hash)
		mail_list_handler.confirm_subscription(test_hash)

		test_result = mail_list_handler.unsubscribe(test_hash)

		self.assertEqual(test_result, "UNSUBSCRIBED")

		mail_list_handler.clear_mail_list()
		return

	def test_broadcast_to_users_success(self):
		mail_list_handler = MailListHandler(mail, current_app)
		mail_list_handler.clear_mail_list()

		test_email = "test1@test.com"
		test_hash = hash_message(test_email)

		mail_list_handler.create_new_sub(test_email, test_hash)
		mail_list_handler.confirm_subscription(test_hash)

		test_email = "test2@test.com"
		test_hash = hash_message(test_email)

		mail_list_handler.create_new_sub(test_email, test_hash)
		mail_list_handler.confirm_subscription(test_hash)

		test_email = "test3@test.com"
		test_hash = hash_message(test_email)

		mail_list_handler.create_new_sub(test_email, test_hash)
		mail_list_handler.confirm_subscription(test_hash)

		with mail.record_messages() as outbox:
			mail_list_handler.broadcast_to_users("title", "excerpt", "url")
			self.assertEqual(len(outbox), 3)


		mail_list_handler.clear_mail_list()
		return


if __name__ == '__main__':
	with app.app_context():
		unittest.main()

