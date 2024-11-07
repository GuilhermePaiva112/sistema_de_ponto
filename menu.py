import flet as ft

def main(page):
    AppBar = ft.AppBar(
        title=ft.Text("Sistema de Ponto Web", size=40),
        center_title=True,
        bgcolor=ft.colors.GREEN_100,
        adaptive=True,
        actions=[
            ft.Column(
                controls=[
                    ft.Text(f'IP: 127.0.0.1'),
                    ft.Text(f'Usuário: Usuário')
                ],
                
            )
        ],
    )

    SideBar = ft.Container(
        bgcolor=ft.colors.GREEN_300,
        margin=-10,
        padding=0,
        width=250,
        height=1000,
    )

    page.add(AppBar)
    page.add(SideBar)

ft.app(target=main)