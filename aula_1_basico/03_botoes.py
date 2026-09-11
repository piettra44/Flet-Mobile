import flet as ft

def main(page: ft.Page):
    # Título que aparece na barra da janela/aba
    page.title = "Formulário simples"

    # Cor de fundo da página inteira: azul marinho escuro
    page.bgcolor = "#eaf4f4"

    # Centraliza os controles no eixo horizontal da página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Padding vertical de 60px (topo e base)
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    # Campo de texto para o nome
    nome = ft.TextField(
        label="Seu nome",
        width=280, # LArgura do campo
        color="#2d3142", # Cor do texto
        # Cor do label "Seu nome"
        label_style=ft.TextStyle(color="#6b7b8c"),
        border_color="#a9c5c6", # Cor da borda
        # Cor quando campo em foco (Clicado ou Ativado)
        focused_border_color="#5fa8a0",
    )

    # CheckBox de aceite dos termos
    aceite = ft.Checkbox(
        label="Aceite os temos",
        check_color="#ffffff",
        active_color="#5fa8a0",
        # Cor do label ("Aceito os termos")
        label_style=ft.TextStyle(color="#2d3142"),
    )

    # Texto de resultado (Após enviar)
    resultado = ft.Text(color="#3e7c7c")

    def enviar(e):
        if not nome.value:
            nome.error_text = "Preencha seu nome"
            page.update()
            return
        nome.error_text = None
        resultado.value = f"Obrigado, {nome.value}!" if aceite.value else "Você precisa aceitar os termos."
        page.update()

    # Construção dos elementos
    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                nome, # Campo nome
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[aceite], # ChackBox (Caixa para marcar ou não)
                ),
                # Botão "Enviar"
                ft.ElevatedButton(
                    "Enviar",
                    on_click=enviar, #Ao clicar chama a função enviar
                    bgcolor="#5fa8a0",
                    color="#ffffff",
                )
            ]
        )
    
    )

ft.run(main)