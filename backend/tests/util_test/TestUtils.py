import unittest
import json
import sys
import os
import pymysql

from flask import current_app

sys.path.append("../../portfolioapi")
from portfolioapi import create_app
from portfolioapi.config import TestConfig
from portfolioapi.utils import *

app = create_app(TestConfig)


class TestUtils(unittest.TestCase):
	def test_DbHelper_connect(self):
		expected = pymysql.connect(host='localhost',
							  user='root',
							  password='',
							  db="portfoliosite",
							  cursorclass=pymysql.cursors.DictCursor)
		test_result = DbHelper.connect()

		self.assertEqual(type(expected), type(test_result))
		return

	def test_ResponseHandler_response_builder_error(self):
		rh = ResponseHandler()

		for status in rh.error_messages:
			test_result = rh.response_builder(status)

			self.assertEqual(test_result["status"], status)
			self.assertEqual(test_result["code"], rh.error_messages[status][0])
			self.assertEqual(test_result["message"], rh.error_messages[status][1])

		return

	def test_ResponseHandler_response_builder_success(self):
		rh = ResponseHandler()

		test_result = rh.response_builder("test success!")

		self.assertEqual(test_result['code'], 200)
		self.assertEqual(test_result['status'], "SUCCESS")
		self.assertEqual(test_result['message'], "Request sucessfully fulfilled.")
		self.assertEqual(test_result['data'], "test success!")
		return

	def test_hash_message(self):
		# Not really sure the best way to test this
		test_message = "Hello There!"

		test_result = hash_message(test_message)

		self.assertNotEqual(test_message, test_result)

		return

	def test_make_json_response(self):
		test_data = {"hello":"there"}
		test_code = 200

		test_result = make_json_response(test_data, test_code)

		self.assertEqual(test_result.status_code, 200)
		self.assertEqual(json.loads(test_result.data), test_data)

		return


if __name__ == '__main__':
	with app.app_context():
		unittest.main()