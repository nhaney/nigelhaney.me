import unittest
import json
import sys
import os

from flask_mail import Mail
from flask import Flask

sys.path.append("../../portfolioapi")
from portfolioapi import create_app
from portfolioapi.config import TestConfig
from portfolioapi.blog.BlogApiHandler import BlogApiHandler
from portfolioapi.blog.BlogTableHandler import BlogTableHandler

app = create_app(TestConfig)
mail = Mail(app)

class TestBlogApiHandler(unittest.TestCase):
	def test_create_post_unauthorized(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = json.dumps({
						 'post_title':'Tesst Post Title',
				 		 'excerpt':'Test Excerpt',
				         'content':'Test Content',
			         })


		test_result = blog_api.create_post(test_data)

		self.assertEqual(test_result['status'], "UNAUTHORIZED_REQUEST")

		return

	def test_create_post_invalid_title(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = json.dumps({
						 'post_title':('TOO_LONG' * 255),
				 		 'excerpt':'Test Excerpt',
				         'content':'Test Content',
				         'auth': app.config['SECRET_KEY']
			         })

		test_result = blog_api.create_post(test_data)

		self.assertEqual(test_result['status'], "INVALID_TITLE")

		test_data = json.dumps({
				 		 'excerpt':'Test Excerpt',
				         'content':'Test Content',
				         'auth': app.config['SECRET_KEY']
			         })

		test_result = blog_api.create_post(test_data)

		self.assertEqual(test_result['status'], "INVALID_TITLE")

		return

	def test_create_post_invalid_content(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = json.dumps({
						 'post_title':'Test Post Title',
				 		 'excerpt':'Test Excerpt',
				         'content':('TOO_LONG' * 65535),
				         'auth': app.config['SECRET_KEY']
			         })

		test_result = blog_api.create_post(test_data)

		self.assertEqual(test_result['status'], "INVALID_CONTENT")

		test_data = json.dumps({
						 'post_title':'Test Post Title',
				 		 'excerpt':'Test Excerpt',
				 		 'auth': app.config['SECRET_KEY']
			         })

		test_result = blog_api.create_post(test_data)

		self.assertEqual(test_result['status'], "INVALID_CONTENT")

		return

	def test_create_post_success(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = json.dumps({
				 'post_title':'Test Post Title',
		 		 'excerpt':'Test Excerpt',
		         'content':'Test Content',
		         'auth': app.config['SECRET_KEY']
	         })

		test_result = blog_api.create_post(test_data)

		self.assertEqual(test_result['status'], "SUCCESS")

		# Delete all posts before starting next test_result
		bth = BlogTableHandler()
		bth.delete_all_blog_posts()
		return

	def test_read_post_invalid(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = None

		test_result = blog_api.read_post(test_data)

		self.assertEqual(test_result['status'], "INVALID_TITLE")

		return

	def test_read_post_success(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = json.dumps({
				 'post_title':'Test Post Title',
		 		 'excerpt':'Test Excerpt',
		         'content':'Test Content',
		         'auth': app.config['SECRET_KEY']
	         })

		blog_api.create_post(test_data)
		test_result = blog_api.read_post("Test Post Title")

		self.assertEqual(test_result['status'], "SUCCESS")

		bth = BlogTableHandler()
		bth.delete_all_blog_posts()
		return

	def test_read_post_doesnt_exist(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = "test"

		test_result = blog_api.read_post(test_data)

		self.assertEqual(test_result['status'], "POST_NOT_FOUND")
		return

	def test_update_post_unauthorized(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = json.dumps({
		 'post_title':'Tesst Post Title',
         'content':'Test Content',
		})

		test_result = blog_api.update_post(test_data)

		self.assertEqual(test_result['status'], "UNAUTHORIZED_REQUEST")
		return

	def test_update_post_invalid_title(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = json.dumps({
			'content':'blahblahblah',
			'auth':app.config['SECRET_KEY']
		})

		test_result = blog_api.update_post(test_data)

		self.assertEqual(test_result['status'], "INVALID_TITLE")

		test_data = json.dumps({
			'post_title':("x" * 50000),
			'content':'blahblahblah',
			'auth':app.config['SECRET_KEY']
		})

		test_result = blog_api.update_post(test_data)

		self.assertEqual(test_result['status'], "INVALID_TITLE")
		return

	def test_update_post_invalid_content(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = json.dumps({
			'post_title':'test title',
			'auth':app.config['SECRET_KEY']
		})

		test_result = blog_api.update_post(test_data)

		self.assertEqual(test_result['status'], "INVALID_CONTENT")

		test_data = json.dumps({
			'post_title':'test title',
			'auth':app.config['SECRET_KEY'],
			'content':("x" * 70000)
		})

		test_result = blog_api.update_post(test_data)

		self.assertEqual(test_result['status'], "INVALID_CONTENT")
		return

	def test_update_post_success(self):
		bth = BlogTableHandler()
		bth.delete_all_blog_posts()

		blog_api = BlogApiHandler(mail, app)

		test_data = json.dumps({
			'post_title':'Test Post Title',
			'excerpt':'Test Excerpt',
			'content':'Test Content',
			'auth': app.config['SECRET_KEY']
		})

		blog_api.create_post(test_data)

		test_data = json.dumps({
			'post_title':'Test Post Title',
			'content':'Updated Test Content',
			'auth':app.config['SECRET_KEY']
		})

		test_result = blog_api.update_post(test_data)

		self.assertEqual(test_result['data']['content'], 
								"Updated Test Content")
		self.assertEqual(blog_api.read_post("Test Post Title")['data']['content'],
				 							"Updated Test Content")


		bth = BlogTableHandler()
		bth.delete_all_blog_posts()
		return


	def test_delete_post_unauthorized(self):
		blog_api = BlogApiHandler(mail, app)
		
		test_data = json.dumps({
			'post_title':'test title',
		})

		test_result = blog_api.delete_post(test_data)

		self.assertEqual(test_result['status'], "UNAUTHORIZED_REQUEST")

		test_data = json.dumps({
			'post_title':'test title',
			'auth':'invalidauthorization'
		})

		test_result = blog_api.delete_post(test_data)

		self.assertEqual(test_result['status'], "UNAUTHORIZED_REQUEST")
		return

	def test_delete_post_invalid(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = json.dumps({
			"not_title":"this is invalid",
			"auth":app.config['SECRET_KEY']
		})

		test_result = blog_api.delete_post(test_data)

		self.assertEqual(test_result['status'], "INVALID_TITLE")

		test_data = json.dumps({
			"post_title":("TOO_LONG" * 255),
			"auth":app.config['SECRET_KEY']
		})

		self.assertEqual(test_result['status'], "INVALID_TITLE")
		return

	def test_delete_post_success(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = json.dumps({
				 'post_title':'Test Post Title',
		 		 'excerpt':'Test Excerpt',
		         'content':'Test Content',
		         'auth': app.config['SECRET_KEY']
	         })

		blog_api.create_post(test_data)

		test_data = json.dumps({
			'post_title':'Test Post Title',
			'auth': app.config['SECRET_KEY']
		})

		test_result = blog_api.delete_post(test_data)

		self.assertEqual(test_result['status'], "SUCCESS")
		self.assertEqual(blog_api.read_post('Test Post Title')['status'],
			"POST_NOT_FOUND")

		return

	def test_create_new_commnent_invalid_post(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = json.dumps({
			"author":"test author",
			"content":"test comment"
		})

		test_result = blog_api.create_new_comment(test_data)

		self.assertEqual(test_result['status'], "POST_NOT_FOUND")

		test_data = json.dumps({
			"post_id":0,
			"author":"test author",
			"content":"test comment"
		})

		test_result = blog_api.create_new_comment(test_data)

		self.assertEqual(test_result['status'], "POST_NOT_FOUND")

		return

	def test_create_new_comment_invalid_author(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = json.dumps({
			"post_id":55,
			"content":"test comment"
		})

		test_result = blog_api.create_new_comment(test_data)

		self.assertEqual(test_result['status'], "INVALID_AUTHOR")

		test_data = json.dumps({
			"author":"",
			"post_id":55,
			"content":"test comment"
		})

		test_result = blog_api.create_new_comment(test_data)

		self.assertEqual(test_result['status'], "INVALID_AUTHOR")

		test_data = json.dumps({
			"author":("TOO LONG" * 255),
			"post_id":55,
			"content":"test comment"
		})

		test_result = blog_api.create_new_comment(test_data)

		self.assertEqual(test_result['status'], "INVALID_AUTHOR")

		return

	def test_create_new_comment_invalid_comment(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = json.dumps({
			"post_id":55,
			"author":"Test"
		})

		test_result = blog_api.create_new_comment(test_data)

		self.assertEqual(test_result['status'], "INVALID_COMMENT_CONTENT")

		test_data = json.dumps({
			"content":("TOO LONG" * 70000),
			"post_id":55,
			"author":"Test"
		})

		test_result = blog_api.create_new_comment(test_data)

		self.assertEqual(test_result['status'], "INVALID_COMMENT_CONTENT")

		test_data = json.dumps({
			"content":"",
			"post_id":55,
			"author":"Test"
		})

		test_result = blog_api.create_new_comment(test_data)

		self.assertEqual(test_result['status'], "INVALID_COMMENT_CONTENT")
		return

	def test_create_new_comment_success(self):
		blog_api = BlogApiHandler(mail, app)
		bth = BlogTableHandler()
		bth.delete_all_blog_posts()


		temp_post_id = bth.create_blog_post("T", "T", "T")['post_id']

		test_data = json.dumps({
			"post_id":temp_post_id,
			"author":"Test Author",
			"content":"Test content"
		})

		test_result = blog_api.create_new_comment(test_data)

		self.assertEqual(test_result['data']['content'], "Test content")
		self.assertEqual(test_result['data']['author'], "Test Author")
		self.assertEqual(test_result['data']['post_id'], temp_post_id)

		bth.delete_all_blog_posts()
		return

	def test_read_comments_from_post_invalid_post(self):
		blog_api = BlogApiHandler(mail, app)

		test_result = blog_api.read_comments_from_post(None)

		self.assertEqual(test_result['status'], "POST_NOT_FOUND")

		test_result = blog_api.read_comments_from_post(67223949234)

		self.assertEqual(test_result['status'], "POST_NOT_FOUND")

		return

	def test_read_comments_from_post_success(self):
		blog_api = BlogApiHandler(mail, app)
		bth = BlogTableHandler()
		bth.delete_all_blog_posts()

		temp_post_id = bth.create_blog_post("T", "T","T")['post_id']

		test_data = json.dumps({
			"post_id":temp_post_id,
			"author":"Test Author",
			"content":"Test content"
		})
		
		blog_api.create_new_comment(test_data)

		test_result = blog_api.read_comments_from_post(temp_post_id)

		self.assertEqual(test_result['data'][0]['content'], "Test content")

		blog_api.create_new_comment(test_data)

		test_result = blog_api.read_comments_from_post(temp_post_id)

		self.assertEqual(len(test_result['data']), 2)

		bth.delete_all_blog_posts()
		return

	def test_delete_comment_by_id_comment_not_found(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = json.dumps({
			"auth":app.config['SECRET_KEY']
		})

		test_result = blog_api.delete_comment_by_id(test_data)

		self.assertEqual(test_result['status'], "COMMENT_NOT_FOUND")

		test_data = json.dumps({
			"comment_id":0,
			"auth":app.config['SECRET_KEY']
		})

		test_result = blog_api.delete_comment_by_id(test_data)

		self.assertEqual(test_result['status'], "COMMENT_NOT_FOUND")
		return

	def test_delete_comment_by_id_unauthorized(self):
		blog_api = BlogApiHandler(mail, app)

		test_data = json.dumps({
			"comment_id":55
		})

		test_result = blog_api.delete_comment_by_id(test_data)

		self.assertEqual(test_result['status'], "UNAUTHORIZED_REQUEST")

		test_data = json.dumps({
			"comment_id":55,
			"auth":"invalid auth"
		})

		test_result = blog_api.delete_comment_by_id(test_data)

		self.assertEqual(test_result['status'], "UNAUTHORIZED_REQUEST")
		return

	def test_delete_comment_by_id_success(self):
		blog_api = BlogApiHandler(mail, app)
		bth = BlogTableHandler()
		bth.delete_all_blog_posts()

		temp_post_id = bth.create_blog_post("T", "T","T")['post_id']

		test_comment = json.dumps({
			"post_id":temp_post_id,
			"author":"Test Author",
			"content":"Test content"
		})
		
		temp_comment_id = blog_api.create_new_comment(test_comment)['data']['comment_id']

		test_data = json.dumps({
			"comment_id":temp_comment_id,
			"auth":app.config['SECRET_KEY']
		})

		test_result = blog_api.delete_comment_by_id(test_data)

		self.assertEqual(test_result['status'], "SUCCESS")
		self.assertEqual(len(blog_api.read_comments_from_post(
							temp_post_id)['data']), 0)
		
		bth.delete_all_blog_posts()
		return


if __name__ == '__main__':
	with app.app_context():
		unittest.main()




