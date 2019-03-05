import unittest
import sys
import requests
import os
import json

sys.path.append("../")
from blogsubmitter import blogsubmitter

class TestBlogSubmitter(unittest.TestCase):
	def test_no_title(self):
		test_result = blogsubmitter(title="",
									excerpt="excerpt",
									md_file="test.md",
									post_url="127.0.0.1:5000")
		self.assertEqual(test_result, "Blog post must have a title.")

		return
	
	def test_no_excerpt(self):
		test_result = blogsubmitter(title="title",
									excerpt="",
									md_file="test.md",
									post_url="127.0.0.1:5000")
		self.assertEqual(test_result, "Blog post must have an excerpt.")
		return

	def test_no_file(self):
		test_result = blogsubmitter(title="title",
									excerpt="excerpt",
									md_file="",
									post_url="127.0.0.1:5000")
		
		self.assertEqual(test_result, "No markdown file specified to send.")
		return

	def test_invalid_file(self):
		test_result = blogsubmitter(title="title",
									excerpt="excerpt",
									md_file="doesnotexist",
									post_url="127.0.0.1:5000")
		
		self.assertEqual(test_result, "Problem opening the file.", test_result)

	def test_requests_error(self):
		test_result = blogsubmitter(title="test title",
					  				excerpt="test excerpt",
					  				md_file="test.md",
					  				post_url="INVALID127.0.0.1:5000/blog/posts")
		self.assertTrue("Error" in test_result)

	def test_success(self):
		requests.delete("http://127.0.0.1:5000/blog/posts", 
						data=json.dumps({"post_title":"test title",
							  "auth":os.environ["PORTFOLIO_SECRET_KEY"]
		}))

		test_result = blogsubmitter(title="test title",
									excerpt="test excerpt",
									md_file="test.md",
									post_url="http://127.0.0.1:5000/blog/posts")
		
		data = test_result.json()

		self.assertEqual(data['code'], 200)

		requests.delete("http://127.0.0.1:5000/blog/posts", 
						data=json.dumps({"post_title":"test title",
							  "auth": os.environ["PORTFOLIO_SECRET_KEY"]
		}))
		
		return

if __name__ == '__main__':
	unittest.main()