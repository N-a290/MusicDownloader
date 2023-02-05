import flet as ft

from views.index_view import IndexView
from views.download_view import DownloadView
from views.settings_view import SettingsView

class Router:
    
    def __init__(self, page, ft) -> None:
        self.page = page
        self.ft = ft
        self.routes = {
            "/": IndexView(page),
            "/download": DownloadView(page),
            "/settings": SettingsView(page)
        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
