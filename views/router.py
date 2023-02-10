import flet as ft

import views.index_view as iv
import views.download_view as dv
import views.settings_view as sv

import backend.downloader as bkd

dv.run_backend = bkd.download_song

class Router:
    
    def __init__(self, page, ft) -> None:
        self.page = page
        self.ft = ft
        self.routes = {
            "/": iv.IndexView(page),
            "/download": dv.DownloadView(page),
            "/settings": sv.SettingsView(page)
        }
        self.body = ft.Container(
            content=self.routes['/'],
            )

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
