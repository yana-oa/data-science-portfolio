from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi as ytapi

yt_video = "https://www.youtube.com/watch?v=3V-MJhJvRWg"

video_id = yt_video.split("=")[1]
print(video_id)

transcript = ytapi.get_transcript(video_id)
print(transcript)