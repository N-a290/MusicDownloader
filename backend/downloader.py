from pytube import YouTube, Playlist, request

import os
from pathlib import Path

request.default_range_size = 500000

def get_playlist_data(url):
    pass

def get_song_data(url):
    pass

def download_playlist(url):
    pass

def download_song(url, save_location, in_progress, on_complete, handle_error):
    try:
        filename = str(Path(save_location).name)
        output_path = str(os.path.split(Path(save_location))[0])
        print(filename)
        print(output_path)
        download = YouTube(url, on_progress_callback=in_progress, on_complete_callback=on_complete)
        stream = download.streams.filter(progressive=True).get_highest_resolution()
        stream.download(filename=filename, output_path=output_path)
        return  
    except:
        error = True
        handle_error()
        return
