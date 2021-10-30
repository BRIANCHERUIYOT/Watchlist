from flask import Flask,Request,jsonify


# Initializing application
app = Flask(__name__)


from app import views

