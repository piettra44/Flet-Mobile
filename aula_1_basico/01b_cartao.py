import flet as ft

def main(page: ft.Page):
    page.title = "Cartão de apresentação"

    # Define o tamanho da tela
    page.window.width = 320
    page.window.height = 600

    # Cor de fundo da Tela
    page.bgcolor = "#000000"

    # Centralizar elementos
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Padding
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    # Criação do elementos da página
    page.add(
        # Nome em destaque
        ft.Text(
            "Pietra Linda",
            size=28,
            weight=ft.FontWeight.BOLD,
            color="#FF6FB5",
            text_align=ft.TextAlign.CENTER,
        ),
        ft.Text(
            "Estudadnte de programação mobile",
            size=14,
            color="#CC0666",
            text_align=ft.TextAlign.CENTER,
        ),
    )

# Inicia a aplicação
ft.run(main)