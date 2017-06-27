from app import app
from flask import render_template, url_for
from . import constants
import pafy
import requests

base_template = 'audio_template.html'

@app.route("/audio/<video_id>")
def index(video_id=None):
  url = constants.video_url.format(video_id=video_id);
  video = pafy.new(url);
  stream = video.getbestaudio(preftype='m4a').url;
  links = get_recommended(video_id)
  return render_template(base_template, audio=stream, links=links)

def get_recommended(video_id):
  params = constants.params
  params['relatedToVideoId'] = video_id
  result = requests.get(constants.search_endpoint, params=params)
  videos = result.json()['items']
  return [{
      'url': url_for('index', video_id=video['id']['videoId']), 
      'title': video['snippet']['title']
    } 
    for video 
    in videos]