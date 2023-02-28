from time import sleep

import flet as ft 


run_backend = None

def DownloadView(page, ft=ft):

    def pick_file_result(e: ft.FilePickerResultEvent):
            selected_path.value = str(pick_file_dialog.result.path) + ".mp3"
            page.update()

    def handle_submit(e):
        if not url_input.value:
            url_input.error_text = "Ingresa una URL"
            page.update()
        else:
            url_input.error_text = None
            run_backend(url_input.value, selected_path.value, in_progress, on_complete, handle_error)
            page.update()

    def in_progress(d):
        if d['status'] == 'downloading':
            try:
                total_bytes = d['total_bytes']
            except KeyError:
                total_bytes = d['total_bytes_estimate']

            time_left = d['eta']
            percent = d['downloaded_bytes'] / total_bytes

            download_complete.value = f"Descargando..."
            timeleft_message.value = f"Tiempo restante => {time_left}"
            progress_bar.value = percent

            page.update()

    def on_complete(*args):
        download_complete.value = "Descarga Completa"
        timeleft_message.value = ""
        page.update()

    def handle_error(*args):
        download_complete.value = "Algo salió mal, intenta de nuevo"
        page.update()

    url_input = ft.TextField(label="URL de la canción")
    pick_file_dialog = ft.FilePicker(on_result=pick_file_result)
    pick_file_button = ft.ElevatedButton(
        "Escoge el nombre del archivo",
        icon=ft.icons.UPLOAD_FILE,
        on_click=lambda _: pick_file_dialog.save_file(
            file_type="audio", 
            allowed_extensions=["mp3"])
        )
    page.overlay.append(pick_file_dialog)
    selected_path = ft.Text()
    selected_path.value = "Ubicación del archivo"

    download_button = ft.TextButton("Descargar", on_click=handle_submit)
    
    download_complete = ft.Text(style="headlineSmall")
    timeleft_message = ft.Text(style="headlineSmall")
    progress_bar = ft.ProgressBar(width=400, value=0)

    content = ft.Column(
            [   
                ft.Row([
                    url_input
                ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row([
                    pick_file_button,
                    selected_path
                    ]),
                ft.Row([
                    download_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER
                    ),
                ft.Column([
                    download_complete,
                    timeleft_message,
                    progress_bar
                ],
                alignment=ft.MainAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=50
        )
    return content