import flet as ft

def main(page):
    
    page.bgcolor=ft.colors.GREEN_100
    page.title = "Sistema de ponto WEB"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    entrada_nome = ft.TextField(
        label="Digite seu CPF", 
        on_change=lambda e: atualizar_botao(), 
        color="#000000", 
        focused_border_color="#000000", 
        label_style=ft.TextStyle(color="#000000")
    )
    
    entrada_senha = ft.TextField(
        label="Digite sua senha", 
        password=True, 
        can_reveal_password=True, 
        on_change=lambda e: atualizar_botao(), 
        color="#000000", 
        focused_border_color="#000000", 
        label_style=ft.TextStyle(color="#000000")
    )
      
    botao_login = ft.ElevatedButton("Acessar", disabled=True)
    
    botao_esqueci_senha = ft.TextButton(text="Esqueci a Senha", on_click=None)
    def atualizar_botao():
        botao_login.disabled = not (entrada_nome.value and entrada_senha.value)
        page.update()


    background_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Ponto Web", size=40, weight=ft.FontWeight.BOLD, color="#000000"),
                                entrada_nome,
                                entrada_senha,
                                botao_login,
                                botao_esqueci_senha
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=35,
                        alignment=ft.alignment.center,
                        width=350,
                        height=350,
                        border_radius=5,
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    page.add(background_container)


ft.app(target=main)