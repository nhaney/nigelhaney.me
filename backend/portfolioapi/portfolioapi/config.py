import os

class Config:
	MAIL_SERVER = "smtp.gmail.com"
	MAIL_PORT = 465
	MAIL_USE_SSL = True
	MAIL_USERNAME = os.environ['GMAIL_USERNAME']
	MAIL_PASSWORD = os.environ['GMAIL_PASSWORD']
	MYSQL_USERNAME = os.environ.get('MYSQL_USERNAME', 'root')
	MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')

	MAIL_SUPRESS_SEND = False
	TESTING = False
	SECRET_KEY = os.environ['PORTFOLIO_SECRET_KEY']
	print("Production mode activated.")


class TestConfig(Config):
	MAIL_DEBUG = True
	TESTING = True
	DEBUG = True
	print("Debug mode activated.")
