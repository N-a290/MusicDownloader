from pytube import YouTube, Playlist, request

import os
from pathlib import Path

request.default_range_size = 500000

def get_playlist_data(url):
    pass

def get_song_data():
    pass

def download_playlist(url):
    pass

def download_song(url, save_location, in_progress, on_complete, handle_error):
    '''
    Problema: Pytube no soporta mp3 y descarga los audios en mp4, esto
    genera que las canciones no salgan completas
    '''

    try:
        filename = str(Path(save_location).name)
        output_path = str(os.path.split(Path(save_location))[0])
        print(filename)
        print(output_path)
        download = YouTube(url, on_progress_callback=in_progress, on_complete_callback=on_complete)
        # stream = download.streams.filter(progressive=True).get_highest_resolution()
        stream = download.streams.filter(only_audio=True).first()
        print(stream)
        # stream.download(filename=filename, output_path=output_path)
        # stream.download(output_path=output_path)
        out_file = stream.download(output_path=output_path)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        return  
    except:
        error = True
        handle_error()
        return

if __name__ == '__main__':
    output_path = r"C:\Users\PC Angel\Music\test.mp4"
    download_song("https://www.youtube.com/watch?v=Ijk4j-r7qPA", output_path, get_song_data, get_song_data, get_song_data)
    