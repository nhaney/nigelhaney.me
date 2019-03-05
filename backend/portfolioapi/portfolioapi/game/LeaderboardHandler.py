import json
import pymysql
import pymysql.cursors
from portfolioapi.utils import DbHelper


class LeaderboardHandler:
	"""
	This class will interact with the various leaderboard MySQL tables.
	"""
	def __init__(self):
		self.connection = None

	def read_fish_leaderboard(self):
		"""
		This function is meant to return all scores in descending order.
		"""

		self.connection = DbHelper.connect()
		result = {}

		try:
			with self.connection.cursor() as cursor:
				sql = "SELECT * FROM fish_leaderboard \
					   ORDER BY (score) DESC;"
				cursor.execute(sql)
				result = cursor.fetchall()
				self.connection.close()
		except pymysql.MySQLError as e:
			print(e, e.args)
			self.connection.close()
			return "DATABASE_ERROR"
		else:
			return result

	def submit_fish_score(self, name, score):
		"""
		This function submits a score to the fish leaderboard and returns it.
		"""
		self.connection = DbHelper.connect()
		result = {}

		try:
			with self.connection.cursor() as cursor:
				sql = "INSERT INTO fish_leaderboard (name, score) \
					   VALUES (%s, %s);"
				cursor.execute(sql,[name, score])
				last_score_id = cursor.lastrowid
				self.connection.commit()
		except pymysql.MySQLError as e:
			print(e, e.args)
			self.connection.close()
			return "DATABASE_ERROR"
		else:
			with self.connection.cursor() as cursor:
				sql = "SELECT * FROM fish_leaderboard WHERE score_id=%s;"
				cursor.execute(sql, [last_score_id])
				result = cursor.fetchone()
			self.connection.close()
			return result

	def clear_fish_leaderboard(self):
		self.connection = DbHelper.connect()
		result = {}

		try:
			with self.connection.cursor() as cursor:
				sql = "DELETE FROM fish_leaderboard;"
				cursor.execute(sql)
				self.connection.commit()
		except pymysql.MySQLError as e:
			print(e, e.args)
			self.connection.close()
			return "DATABASE_ERROR"
		else:
			return "DELETED_ALL_SCORES"



















