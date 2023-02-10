import flet as ft 

def SettingsView(page, ft=ft):

    # def picked_file_display(e : ft.FilePickerResultEvent):
        

    # picker_file = ft.FilePicker(on_result=picked_file_display)
    # selected_path = ft.Text()
    # selected_path.value = "No hay directorio aún"

    content = ft.Column(
        [ft.Text("Escoge el directorio donde se va a estar tu musica:")]
    )
    return content