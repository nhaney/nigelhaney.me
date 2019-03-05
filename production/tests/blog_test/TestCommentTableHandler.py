import unittest
import json
import sys
import os
import pymysql

sys.path.append("../../portfolioapi")
from portfolioapi.blog.BlogTableHandler import BlogTableHandler
from portfolioapi.blog.CommentTableHandler import CommentTableHandler
from portfolioapi.utils import DbHelper

class TestCommentTableHandler(unittest.TestCase):
	def initialize_test_posts(self):
		"""
		This will create posts to test comments on.
		"""

		connection = DbHelper.connect()
		post_ids = []

		with connection.cursor() as cursor:
			try:
				sql = "INSERT INTO blog_posts (unique_url, post_title, excerpt, content) \
					   VALUES (%s, %s, %s, %s);"
				cursor.execute(sql, ["1", "1", "", "Test Content 1"])
				post_ids.append(cursor.lastrowid)

				cursor.execute(sql, ["2", "2", "", "Test Content 2"])
				post_ids.append(cursor.lastrowid)

				cursor.execute(sql, ["3", "3", "", "Test Content 3"])
				post_ids.append(cursor.lastrowid)

				connection.commit()
			except pymysql.MySQLError as e:
				print(e)
				return []
			else:
				return post_ids

	def clear_posts(self):
		"""
		This function will clear out all posts in the blog_posts table
		to use on the next tests.
		"""

		connection = DbHelper.connect()

		with connection.cursor() as cursor:
			try:
				sql = "DELETE FROM blog_posts;"
				cursor.execute(sql)
				connection.commit()
			except:
				print("Something went wrong deleting content from blog_posts table")
			else:
				return

	def test_create_comment_success(self):
		self.clear_posts()
		post_ids = self.initialize_test_posts()

		cth = CommentTableHandler()
		test_result = cth.create_comment(post_ids[0], "Nigel", "Nice post!")

		self.assertEqual(test_result['author'], "Nigel")
		self.assertEqual(test_result['content'], "Nice post!")

		self.clear_posts()
		return

	def test_create_comment_not_found(self):
		cth = CommentTableHandler()

		test_result = cth.create_comment(1, "Nigel", "Nice post!")

		self.assertEqual(test_result, "POST_NOT_FOUND")
		return

	def test_read_comments_success(self):
		self.clear_posts()
		post_ids = self.initialize_test_posts()

		cth = CommentTableHandler()
		cth.create_comment(post_ids[0], "Nigel", "Comment 1")
		cth.create_comment(post_ids[0], "Brenna", "Comment 2")
		cth.create_comment(post_ids[0], "Luke", "Comment 3")
		cth.create_comment(post_ids[0], "Moose", "Comment 4")

		test_result = cth.read_comments(post_ids[0])

		self.assertEqual(len(test_result), 4)
		self.assertEqual(test_result[0]['author'], "Nigel")
		self.assertEqual(test_result[1]['author'], "Brenna")
		self.assertEqual(test_result[2]['author'], "Luke")
		self.assertEqual(test_result[3]['author'], "Moose")

		self.clear_posts()
		return

	def test_read_comments_not_found(self):
		cth = CommentTableHandler()

		test_result = cth.read_comments(1)

		self.assertEqual(test_result, "POST_NOT_FOUND")

		return

	def test_delete_all_comments(self):
		self.clear_posts()
		post_ids = self.initialize_test_posts()
		
		cth = CommentTableHandler()
		cth.create_comment(post_ids[0], "Nigel", "Comment 1")
		cth.create_comment(post_ids[0], "Brenna", "Comment 2")
		cth.create_comment(post_ids[0], "Luke", "Comment 3")
		cth.create_comment(post_ids[0], "Moose", "Comment 4")

		cth.delete_all_comments()

		self.assertFalse(cth.read_comments(post_ids[0]))

		self.clear_posts()
		return

	def test_delete_comment_success(self):
		self.clear_posts()
		post_ids = self.initialize_test_posts()

		cth = CommentTableHandler()
		cth.create_comment(post_ids[0], "Nigel", "Comment 1")
		cth.create_comment(post_ids[0], "Brenna", "Comment 2")
		cth.create_comment(post_ids[0], "Luke", "Comment 3")
		cth.create_comment(post_ids[0], "Moose", "Comment 4")

		comment_ids = [x['comment_id'] for x in cth.read_comments(post_ids[0])]

		delete_message = cth.delete_comment(comment_ids[0])

		test_result = cth.read_comments(post_ids[0])

		self.assertEqual(test_result[0]['author'], 'Brenna')
		self.assertEqual(len(test_result), 3)
		self.assertEqual(delete_message, "COMMENT_DELETED")

		self.clear_posts()
		return

	def test_delete_comment_not_found(self):
		self.clear_posts()
		post_ids = self.initialize_test_posts()

		cth = CommentTableHandler()
		temp_comment = cth.create_comment(post_ids[0], "Nigel", "Comment 1")

		test_result = cth.delete_comment(temp_comment['comment_id'] - 1)

		self.assertEqual(test_result, "COMMENT_NOT_FOUND")

		self.clear_posts()
		return






if __name__ == '__main__':
	unittest.main()



		

		