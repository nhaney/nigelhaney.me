import json
import pymysql
import pymysql.cursors
from portfolioapi.utils import DbHelper


class CommentTableHandler:
	"""
	This class will interact with comments MySQL table.
	It performs all CRUD operations and will be executed by BlogApiHandler
	"""
	def __init__(self):
		self.connection = None

	def create_comment(self, post_id, author, content):
		"""
		This function creates a blog post.
		"""

		self.connection = DbHelper.connect()
		result = {}
		last_comment_id = {}

		try:
			with self.connection.cursor() as cursor:
				# check if post exists
				sql = "SELECT * FROM blog_posts WHERE post_id=%s"
				cursor.execute(sql, [post_id])
				does_exist = cursor.fetchone()
				if not does_exist:
					return "POST_NOT_FOUND"

				sql = "INSERT INTO comments (post_id, author, content) \
					   VALUES (%s, %s, %s);"
				cursor.execute(sql,[post_id, author, content])
				last_comment_id = cursor.lastrowid
				self.connection.commit()
		except pymysql.MySQLError as e:
			self.connection.close()
			return "DATABASE_ERROR"
		else:
			with self.connection.cursor() as cursor:
				sql = "SELECT * FROM comments WHERE comment_id=%s;"
				cursor.execute(sql, [last_comment_id])
				result = cursor.fetchone()
				sql = "UPDATE blog_posts \
					   SET comment_count = comment_count + 1 \
					   WHERE post_id = %s;"
				cursor.execute(sql, [post_id])
				self.connection.commit()
			self.connection.close()
			return result

	def read_comments(self, post_id):
		"""
		This function returns an object that represents the 
		values of the row in the blog_posts table that corresponds
		to the post_id passed into the function
		"""

		self.connection = DbHelper.connect()
		result = {}

		try:
			with self.connection.cursor() as cursor:
					sql = "SELECT * FROM blog_posts WHERE post_id=%s"
					cursor.execute(sql, [post_id])
					does_exist = cursor.fetchone()
					if not does_exist:
						return "POST_NOT_FOUND"

					sql = "SELECT * FROM comments \
						   WHERE post_id=%s \
						   ORDER BY YEAR(published_time), \
						   MONTH(published_time), \
						   DAY(published_time) ASC;"

					cursor.execute(sql, [post_id])
					result = cursor.fetchall()
					self.connection.close()
		except pymysql.MySQLError as e:
			print(e, e.args)
			self.connection.close()
			return "DATABASE_ERROR"
		else:
			return result

	def delete_all_comments(self):
		"""
		Deletes all comments in comments table.
		"""

		self.connection = DbHelper.connect()
		result = {}

		try:
			with self.connection.cursor() as cursor:
				sql = "UPDATE blog_posts \
					   SET comment_count = 0;"
				cursor.execute(sql)
				sql = "DELETE FROM comments;"
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

	# This will need to be added in later after authentication is in place.
	#
	# def update_comment(self, comment_id, new_content):
	# 	"""
	# 	This function updates a blog post
	# 	"""

	# 	self.connection = DbHelper.connect()
	# 	result = {}

	# 	try:
	# 		with self.connection.cursor() as cursor:
	# 			sql = "SELECT * FROM comments WHERE post_title=%s;"
	# 			cursor.execute(sql, [post_title])
	# 			result = cursor.fetchone()
	# 			if result:
	# 				sql = "UPDATE comment \
	# 					   SET content=%s, last_edited=CURRENT_TIMESTAMP \
	# 					   WHERE comment_id=%s;" 
	# 				cursor.execute(sql, [new_content, comment_id])
	# 				self.connection.commit()
	# 			else:
	# 				return "COMMENT_NOT_FOUND"
	# 	except pymysql.MySQLError as e:
	# 		print(e, e.args)
	# 		self.connection.close()
	# 		return "DATABASE_ERROR"
	# 	else:
	# 		with self.connection.cursor() as cursor:
	# 			sql = "SELECT * FROM comments WHERE comment_id=%s;"
	# 			cursor.execute(sql, [comment_id])
	# 			result = cursor.fetchone()

	# 			self.connection.close()
	# 			return result 

	def delete_comment(self, comment_id):
		"""
		This function will delete the blog post specified by the
		post_id argument in the DB.
		"""

		self.connection = DbHelper.connect()
		result = {}

		try:
			# first we see if the post even exists
			with self.connection.cursor() as cursor:
				sql = "SELECT * FROM comments WHERE comment_id=%s;"
				cursor.execute(sql, [comment_id])
				result = cursor.fetchone()

				if result:
					sql = "UPDATE blog_posts \
					   SET comment_count = comment_count - 1 \
					   WHERE post_id = %s;"
					cursor.execute(sql, [result['post_id']])
					sql = "DELETE FROM comments WHERE comment_id=%s;"
					cursor.execute(sql, [comment_id])
					self.connection.commit()
				else:
					return "COMMENT_NOT_FOUND"
		except pymysql.MySQLError as e:
			print(e, e.args)
			self.connection.close()
			return "DATABASE_ERROR"
		else:
			self.connection.close()
			return "COMMENT_DELETED"



















