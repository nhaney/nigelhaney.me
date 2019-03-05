from flask import Blueprint


main = Blueprint('main', __name__)

@main.route('/')
def api_homepage():
	return "Welcome to the api of nigelhaney.me"
