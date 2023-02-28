from pytube import YouTube, Playlist, request
import yt_dlp

import os
from pathlib import Path

request.default_range_size = 500000

def download_song(url, save_location, in_progress, on_complete, handle_error):
    try:
        # Get the name of the folder and file
        filename = str(Path(save_location).name)
        output_path = str(os.path.split(Path(save_location))[0])
        print(filename)
        print(output_path)
        
        # Configurations
        video_info = yt_dlp.YoutubeDL().extract_info(
            url=url, download=False
        )
        options = {
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':f'{output_path}/{filename}',
            'progress_hooks': [in_progress],
        }

        # Downloading phase
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
        print("Download complete... {}".format(filename))
        on_complete()

    except Exception as error:
        print(error)
        handle_error()


def download_video(url, save_location, in_progress, on_complete, handle_error):
    try:
        # Get the name of the folder and file
        filename = str(Path(save_location).name)
        output_path = str(os.path.split(Path(save_location))[0])
        print(filename)
        print(output_path)

        # Create the Youtube object
        download = YouTube(url, on_progress_callback=in_progress, on_complete_callback=on_complete)

        # Get the stream of the video
        stream = download.streams.filter(progressive=True).get_highest_resolution()

        # Download the video
        stream.download(filename=filename, output_path=output_path)
        print("Download complete... {}".format(filename))

    except:
        handle_error()


if __name__ == '__main__':
    pass