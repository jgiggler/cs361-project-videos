from flask import Flask, send_from_directory, jsonify
from pytube import YouTube
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Processing videos!'

def download_youtube_video(url):
    yt = YouTube(url)
    video_stream = yt.streams.filter(res='360p', file_extension='mp3').first()
    video_stream.download('videos')
    
    return video_stream.default_filename


@app.route('/videos')
def list_videos():
    
    video_dir = 'videos'
    video_files = os.listdir(video_dir)
    return jsonify(video_files)

@app.route('/videos/<path:filename>')
def serve_video(filename):
    video_dir = 'videos'
    print(filename)
    return send_from_directory(video_dir, filename)

if __name__ == '__main__':
    # videos = ['https://www.youtube.com/watch?v=SXqfFTmYmT0', 'https://www.youtube.com/watch?v=F1cghFu9zBs', 'https://www.youtube.com/watch?v=p7HKvqRI_Bo']
    # for video in videos:
    #     download_youtube_video(video)
    
    app.run(port=5150)
    