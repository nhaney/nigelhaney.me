import unittest
import sys

sys.path.append("../portfolioapi")
from portfolioapi import create_app
from portfolioapi.config import TestConfig

app = create_app(TestConfig)

from blog_test import TestBlogApiHandler
from blog_test import TestBlogIntegration
from blog_test import TestBlogTableHandler
from blog_test import TestCommentTableHandler

from error_test import ErrorTest

from game_test import TestGameApiHandler
from game_test import TestGameIntegration
from game_test import TestLeaderboardHandler

from mail_test import TestMailListHandler
from mail_test import TestMailIntegration

from util_test import TestUtils

loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(TestBlogApiHandler))
suite.addTests(loader.loadTestsFromModule(TestBlogIntegration))
suite.addTests(loader.loadTestsFromModule(TestBlogTableHandler))
suite.addTests(loader.loadTestsFromModule(TestCommentTableHandler))

suite.addTests(loader.loadTestsFromModule(ErrorTest))

suite.addTests(loader.loadTestsFromModule(TestGameApiHandler))
suite.addTests(loader.loadTestsFromModule(TestGameIntegration))
suite.addTests(loader.loadTestsFromModule(TestLeaderboardHandler))

suite.addTests(loader.loadTestsFromModule(TestMailListHandler))
suite.addTests(loader.loadTestsFromModule(TestMailIntegration))

suite.addTests(loader.loadTestsFromModule(TestUtils))

runner = unittest.TextTestRunner(verbosity=3)

with app.app_context():
	result = runner.run(suite)