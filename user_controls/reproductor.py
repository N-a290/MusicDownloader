import flet as ft

def Reproductor(page, ft=ft):

    text = ft.Text(
        value="Hello, im a message",
        expand=True
    )
    DownBar = ft.Container(
        content=text,
        alignment=ft.alignment.bottom_center,
        expand=True,
        bgcolor=ft.colors.ON_INVERSE_SURFACE
    )

    return DownBar