import flet as ft
from menu import create_menu

def main(page: ft.Page):
    page.title = "Sistema de Ponto"
    
    def chamar(e):
        page.clean()
        
        # Recebe app_bar e sidebar como uma tupla
        app_bar, sidebar = create_menu()
        
        # Adiciona app_bar e sidebar à página ao clicar no botão
        page.add(app_bar)
        page.add(sidebar)
        page.update()
    
    # Botão para chamar o menu
    add = ft.Container(
        content=ft.ElevatedButton('Chamar', on_click=chamar)
    )
    
    page.add(add)
    page.update()

ft.app(target=main)
