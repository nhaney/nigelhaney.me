import json
import os
import html

from portfolioapi.game.LeaderboardHandler import LeaderboardHandler
from portfolioapi.utils import ResponseHandler

class GameApiHandler:
	"""
	This class handles the blog's api calls to the MySQL backend.
	Each different function will be routed through the ApiHandler
	as the HTTP request comes in. It will then dispatch the job
	to the handler that interacts with the correct table.
	"""
	def __init__(self):
		self.lbh = LeaderboardHandler()
		self.rh = ResponseHandler()


	def read_leaderboard(self, game_name):
		"""
		This function will return a list of all scores, 
		sorted in descending order.
		"""
		if game_name == "fish":
			status = self.lbh.read_fish_leaderboard()
		else:
			status = "GAME_NOT_FOUND"

		return self.rh.response_builder(status)

	def submit_to_leaderboard(self, data):
		data_obj = json.loads(data)

		if 'game_name' not in data_obj:
			status = "GAME_NOT_FOUND"
		elif 'name' not in data_obj or len(data_obj['name']) > 25 or not data_obj['name']:
			status = "INVALID_NAME"
		else:
			if data_obj['game_name'] == "fish":
				data_obj['name'] = html.escape(data_obj['name'])
				status = self.lbh.submit_fish_score(data_obj['name'], 
														  data_obj['score'])
			else:
				status = "GAME_NOT_FOUND"

		return self.rh.response_builder(status)















	
