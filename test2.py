import flet as ft
#from menu import create_menu

def create_menu2(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.bgcolor = ft.colors.ORANGE
    app_bar = ft.AppBar(
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

    rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            bgcolor=ft.colors.GREEN_300,
            # min_width=100,
            # min_extended_width=400,
            group_alignment=-1.0,
            extended=True,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, 
                    selected_icon=ft.icons.FAVORITE, 
                    label="Empresa",
                    padding=ft.padding.only(bottom=-10),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, 
                    selected_icon=ft.icons.FAVORITE, 
                    label="Departamento",
                    padding=ft.padding.only(bottom=-10),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, 
                    selected_icon=ft.icons.FAVORITE, 
                    label="Setor",
                    padding=ft.padding.only(bottom=-10),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, 
                    selected_icon=ft.icons.FAVORITE, 
                    label="Função",
                    padding=ft.padding.only(bottom=-10),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, 
                    selected_icon=ft.icons.FAVORITE, 
                    label="Sindicato",
                    padding=ft.padding.only(bottom=-10),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, 
                    selected_icon=ft.icons.FAVORITE, 
                    label="Feriados",
                    padding=ft.padding.only(bottom=-10),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, 
                    selected_icon=ft.icons.FAVORITE, 
                    label="Horários",
                    padding=ft.padding.only(bottom=-10),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, 
                    selected_icon=ft.icons.FAVORITE, 
                    label="Tabela Horário",
                    padding=ft.padding.only(bottom=-10),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, 
                    selected_icon=ft.icons.FAVORITE, 
                    label="Ocorrência",
                    padding=ft.padding.only(bottom=-10),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, 
                    selected_icon=ft.icons.FAVORITE, 
                    label="Eventos Folha",
                    padding=ft.padding.only(bottom=-10),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, 
                    selected_icon=ft.icons.FAVORITE, 
                    label="Período Aponta",
                    padding=ft.padding.only(bottom=-10),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, 
                    selected_icon=ft.icons.FAVORITE, 
                    label="Colaborador",
                    padding=ft.padding.only(bottom=-10),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, 
                    selected_icon=ft.icons.FAVORITE, 
                    label="Marcação Relógio",
                    padding=ft.padding.only(bottom=-10),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, 
                    selected_icon=ft.icons.FAVORITE, 
                    label="Cálculo",
                    padding=ft.padding.only(bottom=-10),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, 
                    selected_icon=ft.icons.FAVORITE, 
                    label="Localização",
                    padding=ft.padding.only(bottom=-10),
                ),
            ],
            on_change=lambda e: print("Selected destination:", e.control.selected_index),
        )

    """def chamar(e):
        page.clean()
        
        # Recebe app_bar e sidebar como uma tupla
        app_bar, sidebar = create_menu(page)
        
        # Adiciona app_bar e sidebar à página ao clicar no botão
        page.add(app_bar)
        page.add(sidebar)
        page.update()"""

    sidebar = ft.Container(
        bgcolor=ft.colors.GREEN_300,
        margin=-10,
        padding=0,
        width=150,
        height=1000,
        content=ft.Container(
            ft.Column(
                controls=[
                    ft.Row(
                        [
                            #ft.ElevatedButton('Chamar', on_click=chamar),
                            rail,
                        ],
                        expand=True,
                    )
                ]   
            ),
        ),
    )

    return app_bar, sidebar