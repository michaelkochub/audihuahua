from app import app
from flask import render_template
import pafy

@app.route("/audio/<video_id>")
def hello_world(video_id=None):
  url = 'https://www.youtube.com/watch?v={video_id}'.format(video_id=video_id);
  video = pafy.new(url);
  stream_url = video.getbestaudio(preftype='m4a').url;
  return render_template('audio_template.html', audio_stream=stream_url)

