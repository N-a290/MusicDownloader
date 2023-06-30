import flet as ft
import os
from pathlib import Path

song_path = ""
song_title = str(Path(song_path).name).replace(".mp3" , "")
audio_controller = ft.Audio(
        volume=1,
        on_loaded=lambda _: print("Loaded"),
        on_duration_changed=lambda e: print("Duration changed:", e.data),
        on_position_changed=lambda e: print("Position changed:", e.data),
        on_state_changed=lambda e: print("State changed:", e.data),
        on_seek_complete=lambda _: print("Seek complete"),
    )
height = 0

def change_song(e: str):
    song_path = e


def Reproductor(page, ft=ft):

    # # Componentes del reproductor
    # thumbnail = ft.Image(src="")
    text_title = ft.Text("No song selected")
    # if (song_path != ""):
    #     audio_controller.src = song_path
    #     text_title.value = song_title



    DownBar = ft.Container(
        content=text_title,
        alignment=ft.alignment.bottom_center,
        bgcolor=ft.colors.ON_INVERSE_SURFACE
    )

    return DownBar

