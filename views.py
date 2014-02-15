#!/usr/bin/python2
from flask import (
	Flask,
	render_template,
	redirect,
	url_for,
	request,
	session
	)
from pymongo import MongoClient
import httplib2, os, sys
from apiclient.discovery import build
from apiclient.errors import HttpError

# Import constants
from constants import MONGODB_HOST, MONGODB_PORT, YT_API_KEY, YT_CHANNEL_NAME

# Create instance of app
app=Flask(__name__)
app.debug=True
app.config.from_object(__name__)

# Connect to database, select collection
connection=MongoClient()
db=connection['wikitongues']

# Connect to and configure YouTube
youtube=build('youtube', 'v3', developerKey=YT_API_KEY)
channel_id=youtube.channels().list(
	part=u"id",
	forUsername=YT_CHANNEL_NAME
).execute()['items'][0]['id']
get_playlists=youtube.playlists().list(
	part=u"id, snippet",
	channelId=channel_id,
	maxResults=50
).execute()

# Test view
@app.route("/")
def mainpage(name=None):
	return render_template('index.html', name=name, get_playlists=get_playlists)

# Run this jawn
if __name__=="__main__":
	app.run()
