import json
import os
import html
from flask import current_app

from portfolioapi.blog.BlogTableHandler import BlogTableHandler
from portfolioapi.blog.CommentTableHandler import CommentTableHandler
from portfolioapi.mail.MailListHandler import MailListHandler
from portfolioapi.utils import ResponseHandler


class BlogApiHandler:
	"""
	This class handles the blog's api calls to the MySQL backend.
	Each different function will be routed through the ApiHandler
	as the HTTP request comes in. It will then dispatch the job
	to the handler that interacts with the correct table.
	"""
	def __init__(self, mail, app):
		self.blog_handler = BlogTableHandler()
		self.comment_handler = CommentTableHandler()
		self.rh = ResponseHandler()
		self.mail_list_handler = MailListHandler(mail, app)

	def create_post(self, data):
		"""
		This function will create a blog post in the database.
		"""
		data_obj = json.loads(data)

		# data verification step
		if 'auth' not in data_obj or data_obj['auth'] != current_app.config['SECRET_KEY']:
			status = "UNAUTHORIZED_REQUEST"
		elif "post_title" not in data_obj or len(data_obj["post_title"]) + \
						(3 * data_obj['post_title'].count(' ')) > 255:
			status = "INVALID_TITLE"
		elif "content" not in data_obj or len(data_obj["content"]) > 65535:
			status = "INVALID_CONTENT"
		else:
			if 'excerpt' not in data_obj:
				data_obj['excerpt'] = ""

			# BlogTableHandler does the work
			status = self.blog_handler.create_blog_post(data_obj['post_title'],
									  data_obj['excerpt'],
									  data_obj['content'])

		if isinstance(status, dict):
			self.mail_list_handler.broadcast_to_users(status['post_title'],
													 status['excerpt'],
													 status['unique_url'])

		return self.rh.response_builder(status)

	def read_post(self, post_title):
		"""
		This function will return the contents of a post.
		"""

		if not post_title:
			status = "INVALID_TITLE"
		else:
			status = self.blog_handler.read_blog_post(post_title)

		return self.rh.response_builder(status)

	def update_post(self, data):
		"""
		This function will update a blog post's content.
		"""
		data_obj = json.loads(data)

		# data verification step
		if 'auth' not in data_obj or data_obj['auth'] != current_app.config['SECRET_KEY']:
			status = "UNAUTHORIZED_REQUEST"
		elif "post_title" not in data_obj or len(data_obj["post_title"]) + \
						(3 * data_obj['post_title'].count(' ')) > 255:
			status = "INVALID_TITLE"
		elif "content" not in data_obj or len(data_obj["content"]) > 65535:
			status = "INVALID_CONTENT"
		else:
			status = self.blog_handler.update_blog_post(data_obj["post_title"], \
												   data_obj["content"])
			if not status:
				status = "POST_NOT_FOUND"

		return self.rh.response_builder(status)

	def delete_post(self, data):
		"""
		This function will completely remove a blog post from the database
		"""
		data_obj = json.loads(data)

		# data verification step
		if 'auth' not in data_obj or data_obj['auth'] != current_app.config['SECRET_KEY']:
			status = "UNAUTHORIZED_REQUEST"
		elif "post_title" not in data_obj or len(data_obj["post_title"]) + \
						(3 * data_obj['post_title'].count(' ')) > 255:
			status = "INVALID_TITLE"
		else:
			status = self.blog_handler.delete_blog_post(data_obj["post_title"])

		return self.rh.response_builder(status)

	def preview_posts(self):
		"""
		This function will return a json with all the information of the posts.
		"""

		status = self.blog_handler.preview_blog_posts()
		return self.rh.response_builder(status)

	def delete_all_posts(self):
		"""
		This function will delete all blog_posts in the database.
		"""

		status = self.blog_handler.delete_all_posts()
		return self.rh.response_builder(status)

	def create_new_comment(self, data):
		"""
		This function is responsible for creating a new comment.
		We need to verify that author is <= 255 characters,
		Content is <= 65535 characters,
		"""
		data_obj = json.loads(data)

		if "post_id" not in data_obj:
			status = "POST_NOT_FOUND"
		elif "author" not in data_obj or len(data_obj["author"]) > 255 or \
										 		  	not data_obj["author"]:
			status = "INVALID_AUTHOR"
		elif "content" not in data_obj or len(data_obj["content"]) > 10000 or \
														not data_obj["content"]:
			status = "INVALID_COMMENT_CONTENT"
		else:
			# escape html tags to prevent javascript injection
			# not actually necessary, react does this by default.
			# Even if react did not escape the html, it would probably be better
			# to do this when reading the comment, not putting it in DB.
			# data_obj['author'] = html.escape(data_obj['author'])
			# data_obj['content'] = html.escape(data_obj['content'])

			status = self.comment_handler.create_comment(data_obj['post_id'],
														 data_obj['author'],
														 data_obj['content'])

		return self.rh.response_builder(status)

	def read_comments_from_post(self, post_id):
		if not post_id:
			status = "POST_NOT_FOUND"
		else:
			status = self.comment_handler.read_comments(post_id)

		return self.rh.response_builder(status)

	def delete_comment_by_id(self, data):
		data_obj = json.loads(data)

		if "comment_id" not in data_obj:
			status = "COMMENT_NOT_FOUND"
		elif "auth" not in data_obj or data_obj["auth"] != current_app.config['SECRET_KEY']:
			status = "UNAUTHORIZED_REQUEST"
		else:
			status = self.comment_handler.delete_comment(data_obj['comment_id'])

		return self.rh.response_builder(status)















	
