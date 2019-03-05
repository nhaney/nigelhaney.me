import json
import pymysql
import pymysql.cursors
from portfolioapi.utils import DbHelper


class BlogTableHandler:
	"""
	This class will interact with blog_posts MySQL table.
	It performs all CRUD operations and will be executed by BlogApiHandler
	"""
	def __init__(self):
		self.connection = None

	def create_blog_post(self, post_title, excerpt, content):
		"""
		This function creates a blog post.
		"""

		self.connection = DbHelper.connect()
		result = {}

		# create unique url for the blog post - the uniqueness will be checked
		# by MySQL in the next step
		unique_url = "blog/" + "%20".join(post_title.split())

		try:
			with self.connection.cursor() as cursor:
				sql = "INSERT INTO blog_posts (unique_url, post_title, excerpt, content) \
					   VALUES (%s, %s, %s, %s)"
				cursor.execute(sql,[unique_url, post_title, excerpt, content])
				self.connection.commit()
		except pymysql.MySQLError as e:
			self.connection.close()
			# Unique field post_title already exists
			if str(e.args[0]) == "1062":
				return "POST_ALREADY_EXISTS"
			else:
				print(e)
				return "DATABASE_ERROR"
		else:
			with self.connection.cursor() as cursor:
				sql = "SELECT * FROM blog_posts WHERE post_title=%s;"
				cursor.execute(sql, [post_title])
				result = cursor.fetchone()
			self.connection.close()
			return result

	def read_blog_post(self, post_title):
		"""
		This function returns an object that represents the 
		values of the row in the blog_posts table that corresponds
		to the post_id passed into the function
		"""

		self.connection = DbHelper.connect()
		result = {}

		try:
			with self.connection.cursor() as cursor:
				sql = "SELECT * FROM blog_posts WHERE post_title=%s;"
				cursor.execute(sql, post_title)
				result = cursor.fetchone()
				self.connection.close()
		except pymysql.MySQLError as e:
			print(e, e.args)
			self.connection.close()
			return "DATABASE_ERROR"
		else:
			if not result:
				return "POST_NOT_FOUND"
			else:
				return result

	def preview_blog_posts(self):
		"""
		This function returns the post_title and excerpt of all posts in the table.
		"""

		self.connection = DbHelper.connect()
		result = {}

		try:
			with self.connection.cursor() as cursor:
				sql = "SELECT * FROM blog_posts \
					   ORDER BY published_time DESC;"

				cursor.execute(sql)
				result = cursor.fetchall()
				self.connection.close()
		except pymysql.MySQLError as e:
			print(e, e.args)
			self.connection.close()
			return "DATABASE_ERROR"
		else:
			if not result:
				return "NO_POSTS_EXIST"
			else:
				return result

	def delete_all_blog_posts(self):
		"""
		Deletes all blog posts.
		"""

		self.connection = DbHelper.connect()
		result = {}

		try:
			with self.connection.cursor() as cursor:
				sql = "DELETE FROM blog_posts;"
				# print(sql)
				cursor.execute(sql)
				self.connection.commit()
		except pymysql.MySQLError as e:
			print(e, e.args)
			self.connection.close()
			return "DATABASE_ERROR"
		else:
			self.connection.close()
			return "POST_DELETED"



	def update_blog_post(self, post_title, new_content):
		"""
		This function updates a blog post
		"""

		self.connection = DbHelper.connect()
		result = {}

		try:
			with self.connection.cursor() as cursor:
				sql = "SELECT * FROM blog_posts WHERE post_title=%s;"
				cursor.execute(sql, [post_title])
				result = cursor.fetchone()

			if result:
				with self.connection.cursor() as cursor:
					sql = "UPDATE blog_posts \
						   SET content=%s, last_edited=CURRENT_TIMESTAMP \
						   WHERE post_title=%s;" 
					cursor.execute(sql, [new_content, post_title])
					self.connection.commit()
			else:
				return "POST_NOT_FOUND"
		except pymysql.MySQLError as e:
			print(e, e.args)
			self.connection.close()
			return "DATABASE_ERROR"
		else:
			with self.connection.cursor() as cursor:
				sql = "SELECT * FROM blog_posts WHERE post_title=%s;"
				cursor.execute(sql, [post_title])
				result = cursor.fetchone()

				self.connection.close()
				return result 

	def delete_blog_post(self, post_title):
		"""
		This function will delete the blog post specified by the
		post_id argument in the DB.
		"""

		self.connection = DbHelper.connect()
		result = {}

		try:
			# first we see if the post even exists
			with self.connection.cursor() as cursor:
				sql = "SELECT * FROM blog_posts WHERE post_title=%s;"
				cursor.execute(sql, [post_title])
				result = cursor.fetchone()

			if result:
				with self.connection.cursor() as cursor:
					sql = "DELETE FROM blog_posts WHERE post_title=%s;"
					# print(sql)
					cursor.execute(sql, [post_title])
					self.connection.commit()
			else:
				return "POST_NOT_FOUND"
		except pymysql.MySQLError as e:
			print(e, e.args)
			self.connection.close()
			return "DATABASE_ERROR"
		else:
			self.connection.close()
			return "POST_DELETED"



















