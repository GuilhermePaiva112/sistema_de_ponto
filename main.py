import flet as ft

def main(page):
    
    page.bgcolor=ft.colors.GREEN_100
    page.title = "Sistema de ponto WEB"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def login (e):
        if entrada_nome.value == "123" and entrada_senha.value == "123": # Verifica se o usuário e a senha condizem com o registro
            page.clean()
        else:
            ...

    # Text Field responsável pelo CPF
    entrada_nome = ft.TextField(
        label="Digite seu CPF", 
        on_change=lambda e: atualizar_botao(), 
        color="#000000", 
        focused_border_color="#000000", 
        label_style=ft.TextStyle(color="#000000")
        # Validar CPF
    )
    
    # Text Field responsável pela senha
    entrada_senha = ft.TextField(
        label="Digite sua senha", 
        password=True, 
        can_reveal_password=True, 
        on_change=lambda e: atualizar_botao(), 
        color="#000000", 
        focused_border_color="#000000", 
        label_style=ft.TextStyle(color="#000000")
    )
      
    botao_login = ft.ElevatedButton("Acessar", on_click=login, disabled=True)
    
    botao_esqueci_senha = ft.TextButton(text="Esqueci a Senha", on_click=None)
    
    def atualizar_botao(): # Verifica se os campos de entrada do CPF e Senha foram preenchidos
        botao_login.disabled = not (entrada_nome.value and entrada_senha.value)
        page.update()


    background_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Card(
                    # Card responsável pela adição dos itens de login
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