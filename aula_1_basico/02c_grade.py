import flet as ft


def card_produto(nome, preco):

    return ft.Container(
        width=140,
        height=140,
        padding=12,
        bgcolor="#fff3e0",
        border_radius=12,

        content=ft.Column(
            # Alinhamento vertical
            alignment=ft.MainAxisAlignment.CENTER,

            # Alinhamento horizontal
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            controls=[
                ft.Icon(
                    ft.Icons.SHOPPING_BAG,
                    size=22,
                    color="#E65100"
                ),

                ft.Text(
                    nome,
                    weight=ft.FontWeight.BOLD,
                    color="#4E342E"
                ),

                ft.Text(
                    f"R$ {preco:.2f}",
                    color="#6D4C41"
                ),
            ],
        ),
    )


def main(page: ft.Page):

    page.title = "Prateleira"

    # Define o tamanho da tela
    page.window.width = 320
    page.window.height = 600

    # Cor de fundo da tela
    page.bgcolor = "#2E1A47"

    # Centra o conteúdo da tela
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Padding interno da tela
    page.padding = ft.Padding(
        top=60,
        left=0,
        bottom=60,
        right=0
    )

    # Tupla (nome, preco)
    produtos = [
        ("Caneta", 3.5),
        ("Caderno", 12.9),
        ("Mochila", 89.9),
        ("Estojo", 24.9),
        ("Régua", 5.0),
        ("Borracha", 2.5),
    ]

    page.add(
        ft.Row(
            # Permite rolar horizontalmente
            scroll=ft.ScrollMode.AUTO,

            # Centraliza os cartões em linha
            alignment=ft.MainAxisAlignment.CENTER,

            # Gera os cards
            controls=[
                card_produto(nome, preco)
                for nome, preco in produtos
            ]
        )
    )


# Inicia a aplicação
ft.run(main)