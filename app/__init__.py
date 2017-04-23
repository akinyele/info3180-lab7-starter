from flask import Flask
from flask_triangle import Triangle

app = Flask(__name__)
Triangle(app)

from app import views