#! /usr/bin/python3

import os, sys, logging


PROJECT_DIR = "/var/www/portfolioapi"
sys.path.insert(0, PROJECT_DIR+"/portfolioapi")
sys.path.insert(0, PROJECT_DIR)
logging.basicConfig(stream=sys.stderr)

# WHEN RUNNING ON APACHE, MAKE SURE os.environ is set HERE
# This is best practice according to Graham Dumpleton, author of
# mod_wsgi


def execfile(filename):
    globals = dict(__file__ = filename)
    exec(open(filename).read(), globals)

activate_this = os.path.join(PROJECT_DIR, "venv/bin", "activate_this.py")
execfile(activate_this)

from portfolioapi.config import Config
from portfolioapi import create_app
app = create_app(Config)
app.run()
