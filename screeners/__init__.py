#app/__init__.py: Flask application isinstance
from flask import Flask

app = Flask(__name__)

from app import routes