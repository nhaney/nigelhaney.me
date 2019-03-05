import unittest
import sys
import json

sys.path.append("../portfolioapi/")
from portfolioapi.game.LeaderboardHandler import LeaderboardHandler

class TestLeaderboardHandler(unittest.TestCase):
	def test_submit_fish_score_success(self):
		lbh = LeaderboardHandler()
		lbh.clear_fish_leaderboard()

		test_result = lbh.submit_fish_score("Nigel", "5")

		self.assertEqual(test_result['name'], "Nigel")
		self.assertEqual(test_result['score'], 5)

		lbh.clear_fish_leaderboard()
		return

	def test_read_fish_leaderboard_success(self):
		lbh = LeaderboardHandler()
		lbh.clear_fish_leaderboard()

		lbh.submit_fish_score("Nigel", "1")
		lbh.submit_fish_score("Brenna", "2")
		lbh.submit_fish_score("Luke", "5")
		lbh.submit_fish_score("Moose", "4")

		test_result = lbh.read_fish_leaderboard()

		self.assertEqual(len(test_result), 4)
		self.assertEqual(test_result[0]['name'], "Luke")
		self.assertEqual(test_result[-1]['name'], "Nigel")

		lbh.clear_fish_leaderboard()
		return

	def test_read_fish_leaderboard_empty(self):
		lbh = LeaderboardHandler()
		lbh.clear_fish_leaderboard()

		test_result = lbh.read_fish_leaderboard()

		self.assertEqual(len(test_result), 0)

		return


if __name__ == '__main__':
	unittest.main()


		



