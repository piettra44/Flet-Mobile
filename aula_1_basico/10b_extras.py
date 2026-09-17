import flet as ft

# Cores de prioridade
PRIORITY_COLOR = {
    "alta": "#FF6B6B",
    "media": "#F2C94C",
    "baixa": "#6FCF97"
}

PRIORITY_LABEL = {
    "alta": "Alta",
    "media": "Média",
    "baixa": "Baixa"
}

# Cores das telas
BG_LISTA = "#161B33"
BG_NOVA = "#241B3D"
BG_DETALHE = "#1B2E3D"
BG_DESTAQUE = "#5C7CFA"


def main(page: ft.Page):
    page.title = "App de Tarefas"

    # Dados iniciais
    tasks: list[dict] = [
        {
            "id": 1,
            "title": "Estudar Flet",
            "description": "Terminar os mini-exercícios da Aula 1.",
            "priority": "alta",
            "done": False
        },
        {
            "id": 2,
            "title": "Revisar POO em Python",
            "description": "Classes, atributos e métodos.",
            "priority": "media",
            "done": False
        },
    ]

    next_id = [3]

    # ==========================================================
    # FUNÇÃO: ATUALIZAR CONTADOR
    # ==========================================================

    def contar_tarefas():
        total = len(tasks)
        concluidas = sum(1 for t in tasks if t["done"])
        return concluidas, total

    # ==========================================================
    # TELA: LISTA DE TAREFAS
    # ==========================================================

    def build_task_row(t: dict) -> ft.Container:

        def ir_para_detalhe(e):
            page.navigate(f"/tarefa/{t['id']}")

        def alternar_concluida(e):
            t["done"] = e.control.value
            page.update()

        titulo = ft.Text(
            t["title"],
            expand=True,
            color="#6E7695" if t["done"] else "#E9ECFB",
            style=ft.TextStyle(
                decoration=(
                    ft.TextDecoration.LINE_THROUGH
                    if t["done"]
                    else None
                )
            ),
        )

        return ft.Container(
            padding=12,
            border_radius=10,
            bgcolor="#232A4D",
            content=ft.Row(
                controls=[
                    ft.Checkbox(
                        value=t["done"],
                        on_change=alternar_concluida,
                        active_color=BG_DESTAQUE,
                    ),

                    ft.Container(
                        width=10,
                        height=10,
                        border_radius=5,
                        bgcolor=PRIORITY_COLOR[t["priority"]],
                    ),

                    titulo,

                    ft.Icon(
                        ft.Icons.CHEVRON_RIGHT,
                        color="#8892C4"
                    ),
                ]
            ),
            on_click=ir_para_detalhe,
        )

    def view_lista() -> ft.View:

        # Campo de busca
        busca = ft.TextField(
            label="Buscar tarefa",
            hint_text="Digite o título da tarefa...",
            prefix_icon=ft.Icons.SEARCH,
            width=340,
            color="#FFFFFF",
            label_style=ft.TextStyle(color="#B7A9E0"),
            border_color="#4A3F7A",
            focused_border_color=BG_DESTAQUE,
        )

        # Contador
        concluidas, total = contar_tarefas()

        contador = ft.Text(
            f"{concluidas} de {total} tarefas concluídas",
            color="#B7A9E0",
            size=15,
        )

        # Lista
        lista_view = ft.ListView(
            expand=True,
            spacing=8,
            width=340,
        )

        # ------------------------------------------------------
        # Atualiza a lista conforme a busca
        # ------------------------------------------------------

        def atualizar_lista(e=None):

            texto_busca = (busca.value or "").strip().lower()

            # Filtra pelo título
            tarefas_filtradas = [
                t for t in tasks
                if texto_busca in t["title"].lower()
            ]

            # Ordena por prioridade:
            # Alta = 0
            # Média = 1
            # Baixa = 2
            ordem_prioridade = {
                "alta": 0,
                "media": 1,
                "baixa": 2
            }

            tarefas_filtradas.sort(
                key=lambda t: ordem_prioridade[t["priority"]]
            )

            # Limpa a lista atual
            lista_view.controls.clear()

            # Adiciona as tarefas filtradas e ordenadas
            for tarefa in tarefas_filtradas:
                lista_view.controls.append(
                    build_task_row(tarefa)
                )

            # Atualiza contador
            concluidas, total = contar_tarefas()

            contador.value = (
                f"{concluidas} de {total} tarefas concluídas"
            )

            page.update()

        busca.on_change = atualizar_lista

        # Monta a lista inicialmente
        atualizar_lista()

        return ft.View(
            route="/",
            appbar=ft.AppBar(
                title=ft.Text("Minhas Tarefas")
            ),
            bgcolor=BG_LISTA,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            padding=ft.Padding(
                top=40,
                bottom=60,
                left=0,
                right=0
            ),
            controls=[
                busca,

                ft.Container(
                    height=15
                ),

                contador,

                ft.Container(
                    height=10
                ),

                lista_view,
            ],

            floating_action_button=ft.FloatingActionButton(
                icon=ft.Icons.ADD,
                on_click=lambda e: page.navigate("/nova"),
                bgcolor=BG_DESTAQUE
            ),
        )

    # ==========================================================
    # TELA: NOVA TAREFA / EDITAR TAREFA
    # ==========================================================

    def view_nova(tarefa_editar=None) -> ft.View:

        # Define se estamos criando ou editando
        modo_edicao = tarefa_editar is not None

        titulo = ft.TextField(
            label="Título",
            width=300,
            color="#FFFFFF",
            value=tarefa_editar["title"] if modo_edicao else "",
            label_style=ft.TextStyle(color="#B7A9E0"),
            border_color="#4A3F7A",
            focused_border_color=BG_DESTAQUE,
        )

        descricao = ft.TextField(
            label="Descrição",
            multiline=True,
            min_lines=3,
            width=300,
            color="#FFFFFF",
            value=tarefa_editar["description"] if modo_edicao else "",
            label_style=ft.TextStyle(color="#B7A9E0"),
            border_color="#4A3F7A",
            focused_border_color=BG_DESTAQUE,
        )

        prioridade = ft.RadioGroup(
            value=tarefa_editar["priority"] if modo_edicao else "media",
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Radio(
                        value="alta",
                        label="Alta",
                        label_style=ft.TextStyle(
                            color="#D8CFF2"
                        ),
                        fill_color=BG_DESTAQUE,
                    ),

                    ft.Radio(
                        value="media",
                        label="Média",
                        label_style=ft.TextStyle(
                            color="#D8CFF2"
                        ),
                        fill_color=BG_DESTAQUE,
                    ),

                    ft.Radio(
                        value="baixa",
                        label="Baixa",
                        label_style=ft.TextStyle(
                            color="#D8CFF2"
                        ),
                        fill_color=BG_DESTAQUE,
                    ),
                ]
            ),
        )

        # ------------------------------------------------------
        # SALVAR / ATUALIZAR
        # ------------------------------------------------------

        def salvar(e):

            if not titulo.value or not titulo.value.strip():
                titulo.error_text = "Informe um título"
                page.update()
                return

            titulo.error_text = None

            # -----------------------------
            # MODO EDIÇÃO
            # -----------------------------

            if modo_edicao:

                tarefa_editar["title"] = titulo.value.strip()
                tarefa_editar["description"] = (
                    descricao.value or ""
                )
                tarefa_editar["priority"] = prioridade.value

                page.navigate(
                    f"/tarefa/{tarefa_editar['id']}"
                )

                page.show_dialog(
                    ft.SnackBar(
                        ft.Text(
                            "Tarefa atualizada com sucesso!"
                        )
                    )
                )

            # -----------------------------
            # MODO NOVA TAREFA
            # -----------------------------

            else:

                tasks.append(
                    {
                        "id": next_id[0],
                        "title": titulo.value.strip(),
                        "description": descricao.value or "",
                        "priority": prioridade.value,
                        "done": False,
                    }
                )

                next_id[0] += 1

                page.navigate("/")

                page.show_dialog(
                    ft.SnackBar(
                        ft.Text(
                            "Tarefa criada com sucesso!"
                        )
                    )
                )

        return ft.View(
            route=(
                f"/editar/{tarefa_editar['id']}"
                if modo_edicao
                else "/nova"
            ),

            appbar=ft.AppBar(
                title=ft.Text(
                    "Editar tarefa"
                    if modo_edicao
                    else "Nova tarefa"
                )
            ),

            bgcolor=BG_NOVA,

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            padding=ft.Padding(
                top=60,
                bottom=60,
                left=0,
                right=0
            ),

            controls=[
                titulo,

                descricao,

                ft.Text(
                    "Prioridade:",
                    color="#D8CFF2"
                ),

                prioridade,

                ft.Button(
                    "Atualizar" if modo_edicao else "Salvar",
                    on_click=salvar,
                    bgcolor=BG_DESTAQUE,
                    color="#161B33",
                ),
            ],
        )

    # ==========================================================
    # TELA: DETALHE DA TAREFA
    # ==========================================================

    def view_detalhe(task_id: int) -> ft.View:

        tarefa = next(
            (t for t in tasks if t["id"] == task_id),
            None
        )

        # ------------------------------------------------------
        # Tarefa não encontrada
        # ------------------------------------------------------

        if tarefa is None:

            return ft.View(
                route=f"/tarefa/{task_id}",

                appbar=ft.AppBar(
                    title=ft.Text(
                        "Tarefa não encontrada"
                    )
                ),

                bgcolor=BG_DETALHE,

                horizontal_alignment=(
                    ft.CrossAxisAlignment.CENTER
                ),

                padding=ft.Padding(
                    top=60,
                    bottom=60,
                    left=0,
                    right=0
                ),

                controls=[
                    ft.Text(
                        "Essa tarefa não existe "
                        "(ou já foi excluída).",
                        color="#D6E8F0"
                    )
                ],
            )

        # ------------------------------------------------------
        # Excluir tarefa
        # ------------------------------------------------------

        def excluir_confirmado(e):

            tasks.remove(tarefa)

            page.pop_dialog()

            page.navigate("/")

            page.show_dialog(
                ft.SnackBar(
                    ft.Text("Tarefa excluída.")
                )
            )

        def cancelar(e):
            page.pop_dialog()

        dialogo = ft.AlertDialog(
            title=ft.Text("Excluir tarefa?"),

            content=ft.Text(
                "Essa ação não pode ser desfeita."
            ),

            actions=[
                ft.TextButton(
                    "Cancelar",
                    on_click=cancelar
                ),

                ft.TextButton(
                    "Excluir",
                    on_click=excluir_confirmado
                ),
            ],
        )

        # ------------------------------------------------------
        # Editar tarefa
        # ------------------------------------------------------

        def editar_tarefa(e):
            page.navigate(
                f"/editar/{tarefa['id']}"
            )

        # ------------------------------------------------------
        # Tela de detalhe
        # ------------------------------------------------------

        return ft.View(
            route=f"/tarefa/{task_id}",

            appbar=ft.AppBar(
                title=ft.Text(
                    "Detalhe da tarefa"
                )
            ),

            bgcolor=BG_DETALHE,

            horizontal_alignment=(
                ft.CrossAxisAlignment.CENTER
            ),

            padding=ft.Padding(
                top=60,
                bottom=60,
                left=0,
                right=0
            ),

            controls=[
                ft.Text(
                    tarefa["title"],
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color="#D6E8F0"
                ),

                ft.Row(
                    alignment=(
                        ft.MainAxisAlignment.CENTER
                    ),

                    controls=[
                        ft.Container(
                            width=12,
                            height=12,
                            border_radius=6,
                            bgcolor=(
                                PRIORITY_COLOR[
                                    tarefa["priority"]
                                ]
                            ),
                        ),

                        ft.Text(
                            f"Prioridade "
                            f"{PRIORITY_LABEL[tarefa['priority']]}",
                            color="#A9C7D6",
                        ),
                    ],
                ),

                ft.Text(
                    tarefa["description"]
                    or "(sem descrição)",
                    color="#D6E8F0",
                    text_align=ft.TextAlign.CENTER,
                ),

                # Botão EDITAR
                ft.Button(
                    "Editar",
                    icon=ft.Icons.EDIT,
                    on_click=editar_tarefa,
                    bgcolor=BG_DESTAQUE,
                    color="#161B33",
                ),

                # Botão EXCLUIR
                ft.Button(
                    "Excluir",
                    icon=ft.Icons.DELETE,
                    on_click=lambda e: page.show_dialog(
                        dialogo
                    ),
                    bgcolor="#FF6B6B",
                    color="#1B2E3D",
                ),
            ],
        )

    # ==========================================================
    # ROTEAMENTO
    # ==========================================================

    def route_change(e):

        # Reconstrói a pilha de views
        page.views.clear()

        # A lista sempre fica como primeira tela
        page.views.append(
            view_lista()
        )

        # ------------------------------------------------------
        # NOVA TAREFA
        # ------------------------------------------------------

        if page.route == "/nova":

            page.views.append(
                view_nova()
            )

        # ------------------------------------------------------
        # EDITAR TAREFA
        # ------------------------------------------------------

        troute = ft.TemplateRoute(
            page.route
        )

        if troute.match("/editar/:id"):

            task_id = int(troute.id)

            tarefa = next(
                (
                    t for t in tasks
                    if t["id"] == task_id
                ),
                None
            )

            if tarefa is not None:

                page.views.append(
                    view_nova(tarefa)
                )

        # ------------------------------------------------------
        # DETALHE DA TAREFA
        # ------------------------------------------------------

        troute = ft.TemplateRoute(
            page.route
        )

        if troute.match("/tarefa/:id"):

            task_id = int(troute.id)

            page.views.append(
                view_detalhe(task_id)
            )

        page.update()

    # ==========================================================
    # VOLTAR
    # ==========================================================

    def view_pop(e):

        if len(page.views) > 1:

            page.views.pop()

            page.navigate(
                page.views[-1].route
            )

    # ==========================================================
    # CONFIGURAÇÃO DO FLET
    # ==========================================================

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change(None)


ft.run(main)