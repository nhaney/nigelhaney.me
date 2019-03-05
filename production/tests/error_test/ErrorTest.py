import unittest
import sys
import json

sys.path.append("../../portfolioapi")
from portfolioapi import create_app
from portfolioapi.config import TestConfig

app = create_app(TestConfig)


class ErrorTest(unittest.TestCase):
	def test_not_found(self):
		with app.test_client() as client:
			response = client.get("/invalidpath")
			test_result = json.loads(response.data)
			self.assertEqual(test_result['code'], 404)
			return

	def test_rate_limit(self):
		with app.test_client() as client:
			for _ in range(5):
				client.post("/blog/comments",
							json={
								'post_id':0,
								'author':'Test',
								'content':'Test'
							})

			response = client.post("/blog/comments",
							json={
								'post_id':0,
								'author':'Test',
								'content':'Test'
							})

			test_result = json.loads(response.data)

			self.assertEqual(test_result['code'], 429)

			return

if __name__ == '__main__':
	unittest.main()