from flask import Flask
from flask_mail import Mail
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from portfolioapi.config import Config

app_mail = Mail()
limiter = Limiter(key_func=get_remote_address)

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	app_mail.init_app(app)
	limiter.init_app(app)

	from portfolioapi.blog.routes import blog
	from portfolioapi.game.routes import game
	from portfolioapi.mail.routes import mail
	from portfolioapi.main.routes import main
	from portfolioapi.errors.handlers import errors

	app.register_blueprint(blog)
	app.register_blueprint(game)
	app.register_blueprint(mail)
	app.register_blueprint(main)
	app.register_blueprint(errors)

	return app

