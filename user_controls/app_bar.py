import flet as ft

def NavBar(page, ft=ft):

    NavBar = ft.AppBar(
        leading= ft.Icon(ft.icons.FACE_OUTLINED),
        leading_width= 40,
        title= ft.Text("MyMusicDownloader"),
        center_title= True,
        bgcolor= ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go("/")),
            ft.IconButton(ft.icons.DOWNLOAD_ROUNDED, on_click=lambda _: page.go("/download")),
            ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click=lambda _: page.go("/settings"))
        ]
    )

    return NavBar