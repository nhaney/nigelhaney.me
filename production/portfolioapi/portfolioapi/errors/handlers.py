from flask import Blueprint
from portfolioapi.utils import make_json_response

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(429)
def ratelimit_handler(e):
	return make_json_response({
		"code":429,
		"message":"You have made too many submissions. You have been rate-limited.",
		"status":"RATE_LIMIT_EXCEEDED"
	}, 429)

@errors.app_errorhandler(404)
def not_found_handler(e):
	return make_json_response({
		"code":404,
		"message":"Bad path, resource not found.",
		"status":"NOT_FOUND"
	}, 404)