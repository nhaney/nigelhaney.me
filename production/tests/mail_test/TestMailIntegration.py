import unittest
import sys
import json

sys.path.append("../../portfolioapi")
from portfolioapi import create_app
from portfolioapi.config import TestConfig

app = create_app(TestConfig)

class TestMailIntegration(unittest.TestCase):
	def test_get_posts_handler(self):
		with app.test_client() as client:
			response = client.get("/blog/posts")
			test_result = json.loads(response.data)
			self.assertNotEqual(test_result, None)
			return

	def test_subscribe_to_mail_list(self):
		with app.test_client() as client:
			response = client.post("/mail/subscribe",
								    json={
								    	'email':'test'
								    })
			test_result = json.loads(response.data)
			self.assertNotEqual(test_result, None)
			return

	def test_confirm_subscription(self):
		with app.test_client() as client:
			response = client.get("/mail/confirm/123")

			test_result = response.status_code

			self.assertNotEqual(test_result, None)
			return

	def test_unsubscribe(self):
		with app.test_client() as client:
			response = client.get("/mail/unsubscribe/123")

			test_result = response.status_code

			self.assertNotEqual(test_result, None)
			return

if __name__ == '__main__':
	with app.app_context():
		unittest.main()
