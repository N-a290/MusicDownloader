import flet as ft
# import logging
# logging.basicConfig(level=logging.DEBUG)

from views.router import Router
from user_controls.app_bar import NavBar
from user_controls.reproductor import Reproductor

def main(page : ft.Page):
    # Page initialization
    page.theme_mode = "dark"

    page.title = "Music Downloader"
    page.window_height = 700
    page.window_width = 600

    # Page Components
    page.appbar = NavBar(page, ft)
    myRouter = Router(page,ft)
    reproductor = Reproductor(page, ft)
    page.on_route_change = myRouter.route_change

    page.add(
        myRouter.body,
        reproductor
    )
    
    page.go('/')


ft.app(target=main, assets_dir='assets')