import flet as ft
from menu import create_menu
def create_olamundo(page):
    def chamar(e):
        page.clean()
        add_menu = create_menu
        page.add(add_menu)
        page.update()
    
    add = ft.Container(
        content=(
            ft.ElevatedButton(f'Chamar', on_click=chamar)
        )
    )
    page.add(add)

ft.app(create_olamundo)