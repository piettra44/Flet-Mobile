import flet as ft

def main(page: ft.Page):
    # Configurações iniciais
    page.title="Modo Claro/Escuro"
    # Inicia no mode Claro
    page.theme_mode = ft.ThemeMode.LIGHT 
    # Alinha tudo ao centro
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Função que redesenha toda a tela se o tema for trocado
    def construir_tela():
        # Limpa a tela antes de recriar o app
        page.controls.clear

        # Troca para o modo escuro
        escuro = page.theme_mode == ft.ThemeMode.DARK

        # Define o ícone cores e texto de acordo com o tema atual
        icone = ft.Icon(
            ft.Icons.LIGHT_MODE if escuro else ft.Icons.DARK_MODE,
            size=60,
            color=ft.Colors.AMBER if escuro else ft.Colors.BLUE_200,
        )
        texto = ft.Text(
            "Modo Escuro ativado!" if escuro else "Modo claro ativado!",
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE if escuro else ft.Colors.BLACK,
        )
        botao = ft.ElevatedButton(
            "Ativar Modo Claro" if escuro else "Ativar Modo Escuro",
            on_click=alternar_tema,
        )

        page.bgcolor= ft.Colors.BLACK if escuro else ft.Colors.WHITE

        # Adicionamos os elementos centralizados
        page.add(
            ft.Column(
                [ft.Container(height=60), icone, texto, botao],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )

        page.update()


    def alternar_tema(e):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )

        construir_tela()
    construir_tela() # Chama a tela pena primeira vez

# Inicia o app
ft.app(target=main)