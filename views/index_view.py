import flet as ft 

def IndexView(page, ft=ft):

    content = ft.Column(
        [
            ft.ListView(
                [
                    ft.Text("No hay nada aún", style='labelMedium')
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )
    return content
