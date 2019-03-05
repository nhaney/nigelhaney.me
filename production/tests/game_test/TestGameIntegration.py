import unittest
import sys
import json

sys.path.append("../../portfolioapi")
from portfolioapi import create_app
from portfolioapi.config import TestConfig
from portfolioapi.game.LeaderboardHandler import LeaderboardHandler

app = create_app(TestConfig)

class TestGameIntegration(unittest.TestCase):
	def test_get_high_scores(self):
		with app.test_client() as client:
			response = client.get("/game/fish")
			test_result = json.loads(response.data)
			self.assertNotEqual(test_result, None)
			return

	def test_post_score(self):
		with app.test_client() as client:
			lbh = LeaderboardHandler()
			lbh.clear_fish_leaderboard()

			response = client.post('/game', json={
				'game_name':"fish",
				"name":"test",
				"score":50
			})
			test_result = json.loads(response.data)
			self.assertNotEqual(test_result, None)
			
			lbh.clear_fish_leaderboard()
			return


if __name__ == '__main__':
	with app.app_context():
		unittest.main()
