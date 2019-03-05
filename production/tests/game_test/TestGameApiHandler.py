import unittest
import json
import sys
import os

sys.path.append("../portfolioapi/")
from portfolioapi.game.GameApiHandler import GameApiHandler
from portfolioapi.game.LeaderboardHandler import LeaderboardHandler

class TestGameApiHandler(unittest.TestCase):
	def test_read_leaderboard_game_not_found(self):
		test_input = "invalid game name"
		gah = GameApiHandler()

		test_result = gah.read_leaderboard(test_input)

		self.assertEqual(test_result['status'], "GAME_NOT_FOUND")

		return

	def test_read_leaderboard_game_success(self):
		test_input = "fish"

		gah = GameApiHandler()
		gah.lbh.clear_fish_leaderboard()
		gah.lbh.submit_fish_score("Nigel", 1)
		gah.lbh.submit_fish_score("Brenna", 4)
		gah.lbh.submit_fish_score("Moose", 3)
		gah.lbh.submit_fish_score("Luke", 2)

		test_result = gah.read_leaderboard(test_input)

		self.assertEqual(test_result['status'], "SUCCESS")
		self.assertEqual(test_result['data'][0]['name'], "Brenna")
		self.assertEqual(test_result['data'][-1]['name'], "Nigel")
		self.assertEqual(test_result['data'][-1]['score'], 1)

		gah.lbh.clear_fish_leaderboard()
		return

	def test_submit_to_leaderboard_invalid_name(self):
		test_input = json.dumps({
			'score':420,
			'game_name':'fish'
		})

		gah = GameApiHandler()
		gah.lbh.clear_fish_leaderboard()

		test_result = gah.submit_to_leaderboard(test_input)

		print(test_result)

		self.assertEqual(test_result['status'], "INVALID_NAME")

		test_input = json.dumps({
			'name': ("x" * 26),
			'score': 420,
			'game_name':'fish'
		})

		gah.lbh.clear_fish_leaderboard()

		test_result = gah.submit_to_leaderboard(test_input)

		self.assertEqual(test_result['status'], "INVALID_NAME")

		gah.lbh.clear_fish_leaderboard()
		return

	def test_submit_to_leaderboard_invalid_game(self):
		test_input = json.dumps({
			'name':'Nigel',
			'score':420,
			'game_name':'invalid game name'
		})

		gah = GameApiHandler()
		gah.lbh.clear_fish_leaderboard()

		test_result = gah.submit_to_leaderboard(test_input)

		self.assertEqual(test_result['status'], "GAME_NOT_FOUND")

		test_input = json.dumps({
			'name':'Nigel',
			'score':420
		})

		gah.lbh.clear_fish_leaderboard()

		test_result = gah.submit_to_leaderboard(test_input)

		self.assertEqual(test_result['status'], "GAME_NOT_FOUND")

		gah.lbh.clear_fish_leaderboard()
		return

	def test_submit_to_leaderboard_success(self):
		test_input = json.dumps({
			'name':'Nigel',
			'score':420,
			'game_name':'fish'
		})

		gah = GameApiHandler()
		gah.lbh.clear_fish_leaderboard()

		test_result = gah.submit_to_leaderboard(test_input)

		self.assertEqual(test_result['status'], "SUCCESS")
		self.assertEqual(test_result['data']['name'], "Nigel")
		self.assertEqual(test_result['data']['score'], 420)

		gah.lbh.clear_fish_leaderboard()
		return


if __name__ == '__main__':
	unittest.main()









