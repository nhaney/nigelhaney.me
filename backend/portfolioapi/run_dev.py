from portfolioapi import create_app
from portfolioapi.config import TestConfig

app = create_app(config_class=TestConfig)

if __name__ == '__main__':
	app.run()