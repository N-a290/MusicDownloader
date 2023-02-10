import flet as ft 

def IndexView(page, ft=ft):
    # list_songs = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    # songs = []
    def picked_file(e : ft.FilePickerResultEvent):
        pick_file_dialog.value = str(file_picker.result.path)
        page.update()

    pick_file_dialog = ft.Text()
    pick_file_dialog.value = "No carpeta"
    file_picker = ft.FilePicker(on_result=picked_file)
    pick_file_button = ft.ElevatedButton(
            "Escoge un directorio",
            icon=ft.icons.FILE_OPEN_ROUNDED,
            on_click=lambda _: file_picker.get_directory_path()
        )
    page.overlay.append(file_picker)

    content = ft.Column(
        [
            ft.ListView(
                [
                    ft.Row([
                        pick_file_dialog,
                        pick_file_button
                    ])
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )
    return content
