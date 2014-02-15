#!/usr/bin/python2
from flask import (
	Flask,
	render_template,
	redirect,
	url_for,
	request,
	session
	)
from mongokit import Connection, Document

# MongoDB configuration
MONGODB_HOST='localhost'
MONGODB_PORT=27017

# Create instance of app
app=Flask(__name__)
app.debug=True
app.config.from_object(__name__)

# Connect to database
connection=Connection(app.config['MONGODB_HOST'], app.config['MONGODB_PORT'])
