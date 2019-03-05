import unittest
import sys
import json

sys.path.append("../../portfolioapi")
from portfolioapi import create_app
from portfolioapi.config import TestConfig
from portfolioapi.blog.BlogTableHandler import BlogTableHandler

app = create_app(TestConfig)

class TestBlogIntegration(unittest.TestCase):
	def test_get_posts_handler(self):
		with app.test_client() as client:
			response = client.get("/blog/posts")
			test_result = json.loads(response.data)
			self.assertNotEqual(test_result, None)
			return

	def test_get_post_handler(self):
		with app.test_client() as client:
			response = client.get("/blog/posts/test")
			test_result = json.loads(response.data)
			self.assertNotEqual(test_result, None)
			return

	def test_create_post_handler_success(self):
		with app.test_client() as client:
			bth = BlogTableHandler()
			bth.delete_all_blog_posts()

			response = client.post('/blog/posts', json={
				'post_title':"test",
				"excerpt":"test",
				"content":"test",
				"auth":app.config['SECRET_KEY']
			})
			test_result = json.loads(response.data)
			self.assertNotEqual(test_result, None)
			
			bth.delete_all_blog_posts()
			return

	def test_update_post_handler_success(self):
		with app.test_client() as client:
			bth = BlogTableHandler()
			bth.delete_all_blog_posts()

			response = client.post('/blog/posts', json={
				"post_title":"test",
				"content":"test",
				"auth":app.config['SECRET_KEY']
			})

			test_result = json.loads(response.data)
			self.assertNotEqual(test_result, None)

			bth.delete_all_blog_posts()
			return

	def test_delete_post_handler_success(self):
		with app.test_client() as client:
			bth = BlogTableHandler()
			bth.delete_all_blog_posts()

			response = client.post('/blog/posts', json={
				"post_title":"test",
				"auth":app.config['SECRET_KEY']
			})

			test_result = json.loads(response.data)
			self.assertNotEqual(test_result, None)

			bth.delete_all_blog_posts()
			return

	def test_create_comment_handler_success(self):
		with app.test_client() as client:
			bth = BlogTableHandler()
			bth.delete_all_blog_posts()

			response = client.post('/blog/comments', json={
				"post_id":0,
				"content":"test",
				"author":"test author"
			})

			test_result = json.loads(response.data)
			self.assertNotEqual(test_result, None)

			bth.delete_all_blog_posts()
			return

	def test_get_comments_handler_success(self):
		with app.test_client() as client:
			bth = BlogTableHandler()
			bth.delete_all_blog_posts()

			response = client.get('/blog/comments/3')

			test_result = json.loads(response.data)
			self.assertNotEqual(test_result, None)

			bth.delete_all_blog_posts()
			return

	def test_delete_comment_handler_success(self):
		with app.test_client() as client:
			bth = BlogTableHandler()
			bth.delete_all_blog_posts()

			response = client.delete('/blog/comments/', json={
				"comment_id":3,
				"auth":app.config['SECRET_KEY']
			})

			test_result = json.loads(response.data)
			self.assertNotEqual(test_result, None)

			bth.delete_all_blog_posts()
			return

if __name__ == '__main__':
	with app.app_context():
		unittest.main()
