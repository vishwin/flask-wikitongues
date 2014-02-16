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
import httplib2, os, sys, random
from apiclient.discovery import build
from apiclient.errors import HttpError

# Import constants
from constants import MONGODB_HOST, MONGODB_PORT, YT_API_KEY, YT_CHANNEL_NAME

# Create instance of app
app=Flask(__name__)
app.debug=True
app.config.from_object(__name__)

# Connect to database, select db
connection=MongoClient()
db=connection['wikitongues']

# Connect to and configure YouTube
youtube=build('youtube', 'v3', developerKey=YT_API_KEY)

channel_data=youtube.channels().list(
	part=u"id, contentDetails",
	forUsername=YT_CHANNEL_NAME
).execute()['items'][0]
uploads_id=channel_data['contentDetails']['relatedPlaylists']['uploads']

# Get playlists
get_playlists=youtube.playlists().list(
	part=u"id, snippet",
	channelId=channel_data['id'],
	maxResults=50
).execute()

# Get videos in playlist
def get_videos(playlist_id):
	return youtube.playlistItems().list(
		part=u"snippet, contentDetails",
		playlistId=playlist_id,
		maxResults=50
	)
	
# Build master list of videos to pick from
video_master=[]
video_list_request=get_videos(uploads_id)
while video_list_request:
	video_list_response=video_list_request.execute()
	for video in video_list_response['items']:
		video_master.append({"title": video['snippet']['title'], "videoID": video['contentDetails']['videoId']})
	
	# Iterate
	video_list_request=youtube.playlistItems().list_next(video_list_request, video_list_response)

# Get thumbnails
def get_thumb(item_id, size):
	return youtube.videos().list(
		part=u"snippet",
		id=item_id
	).execute()['items'][0]['snippet']['thumbnails'][size]['url']

# Test view
@app.route("/")
def mainpage():
	# Seed random number generator
	random.seed()	
	
	# Pick eleven videos, with the last for the main viewport
	picked_videos=[]
	for i in range(11):
		picked_videos.append(video_master[random.randint(0, len(video_master))])
	
	return render_template('index.html', db=db, len=len, picked_videos=picked_videos, thumb=get_thumb)

# Run this jawn
if __name__=="__main__":
	app.run()
