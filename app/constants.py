from app.secret import api_key

search_endpoint = 'https://www.googleapis.com/youtube/v3/search'
video_url = 'https://www.youtube.com/watch?v={video_id}'

# query params to search that remain constant over requests
params = {
  'key': api_key,
  'part': 'snippet',
  'type': 'video'
  'maxResults': 10
}