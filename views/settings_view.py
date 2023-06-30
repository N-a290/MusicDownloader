import flet as ft 
import configparser

def SettingsView(page, ft=ft):
    
    # def pick_file_result(e: ft.FilePickerResultEvent):
    #     selected_directory.value = directory + ".mp3"
    #     page.update()

    # # Define the config file
    # config = configparser.ConfigParser()
    # config.add_section("User configurations")
    # config.set("User configurations", "Directory", directory)

    # with open('config.ini', 'w') as config_file:
    #       config.write(config_file)
    
    # config_data = config.read('config.ini')

    # # File picker logic
    # pick_file_dialog = ft.FilePicker(on_result=pick_file_result)
    
    # pick_file_button = ft.ElevatedButton(
    #     "Escoger",
    #     icon=ft.icons.FOLDER_OPEN_OUTLINED,
    #     on_click=lambda _: pick_file_dialog.get_directory_path()
    #     )
    # page.overlay.append(pick_file_dialog)
    # directory = str(pick_file_dialog.result.path)

    # selected_directory = ft.Text(style='headlineSmall')
    # selected_directory.value = config_data["Directory"]


    # View Content
    content = ft.Column(
        [
            ft.Text("Escoge el directorio donde se va a estar tu musica:"),
            # pick_file_button,
            # selected_directory
        ],
        spacing=50
    )

    # # Testing
    # print(f"directory = {directory}")
    # print(f"config_data = {config_data}")
    return content