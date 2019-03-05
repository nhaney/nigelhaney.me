from flask import Blueprint, request

from portfolioapi import limiter
from portfolioapi.game.GameApiHandler import GameApiHandler
from portfolioapi.utils import make_json_response

game = Blueprint('game', __name__)
game_api_handler = GameApiHandler()

@game.route("/game/<game_name>", methods=['GET'])
def get_high_scores(game_name):
	result = game_api_handler.read_leaderboard(game_name)
	return make_json_response(result, result['code'])

@game.route("/game", methods=['POST'])
@limiter.limit("1000/day;200/hour;50/minute;1/second")
def post_score():
	result = game_api_handler.submit_to_leaderboard(request.data)
	return make_json_response(result, result['code'])
