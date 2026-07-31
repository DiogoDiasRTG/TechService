import flet as ft

from src.models.cliente import Cliente
from src.models.equipamento import Equipamento
from src.models.ordem_servico import OrdemServico
from src.repositories import cliente_repository
from src.repositories import equipamento_repository
from src.repositories import ordem_servico_repository

COR_PRINCIPAL = "#2563EB"       # azul vivo, mas não gritante
COR_FUNDO = "#F3F4F6"           # cinza muito claro, neutro
COR_CARTAO = "#FFFFFF"
COR_BORDA = "#E5E7EB"
COR_TEXTO_TITULO = "#111827"    # quase preto, bom contraste
COR_TEXTO_SUAVE = "#4B5563"     # cinza médio, legível mas discreto


def main(page: ft.Page):
    page.title = "TechService"
    page.bgcolor = COR_FUNDO
    page.scroll = ft.ScrollMode.AUTO
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 24

    def avisar(mensagem):
        page.show_dialog(ft.SnackBar(content=ft.Text(mensagem)))

    def secao(titulo, conteudo):
        return ft.Container(
            width=360,
            bgcolor=COR_CARTAO,
            border_radius=16,
            border=ft.Border(
                top=ft.BorderSide(1, COR_BORDA),
                right=ft.BorderSide(1, COR_BORDA),
                bottom=ft.BorderSide(1, COR_BORDA),
                left=ft.BorderSide(1, COR_BORDA),
            ),
            padding=22,
            content=ft.Column([
                ft.Text(titulo, size=17, weight=ft.FontWeight.BOLD, color=COR_TEXTO_TITULO),
                ft.Divider(height=14, color=COR_FUNDO),
                conteudo,
            ]),
        )

    # ================= CLIENTES =================
    campo_nome = ft.TextField(label="Nome", expand=True, dense=True)
    campo_telefone = ft.TextField(label="Telefone", expand=True, dense=True)
    campo_email = ft.TextField(label="Email", expand=True, dense=True)

    lista_clientes = ft.ListView(spacing=2, height=120)

    def carregar_clientes():
        lista_clientes.controls.clear()
        for c in cliente_repository.listar():
            lista_clientes.controls.append(
                ft.Text(f'{c["nome"]}  -  {c["telefone"]}', size=13, color=COR_TEXTO_SUAVE)
            )

    def inserir_cliente_click(e):
        if not campo_nome.value or not campo_telefone.value:
            avisar("Preenche nome e telefone.")
            return

        cliente = Cliente(nome=campo_nome.value, telefone=campo_telefone.value,
                           email=campo_email.value or None)
        cliente_repository.inserir(cliente)

        campo_nome.value = ""
        campo_telefone.value = ""
        campo_email.value = ""

        carregar_clientes()
        page.update()
        avisar("Cliente inserido com sucesso.")

    conteudo_clientes = ft.Column([
        campo_nome,
        campo_telefone,
        campo_email,
        ft.Row([ft.OutlinedButton("Adicionar cliente",
                                   on_click=inserir_cliente_click,
                                   style=ft.ButtonStyle(color=COR_PRINCIPAL))],
               alignment=ft.MainAxisAlignment.END),
        lista_clientes,
    ], spacing=10)

    # ================= EQUIPAMENTOS =================
    campo_id_cliente = ft.TextField(label="ID do cliente", expand=True, dense=True)
    campo_tipo = ft.TextField(label="Tipo", expand=True, dense=True)
    campo_marca = ft.TextField(label="Marca", expand=True, dense=True)
    campo_modelo = ft.TextField(label="Modelo", expand=True, dense=True)
    campo_serie = ft.TextField(label="Nº de série", expand=True, dense=True)

    lista_equipamentos = ft.ListView(spacing=2, height=120)

    def carregar_equipamentos():
        lista_equipamentos.controls.clear()
        for eq in equipamento_repository.listar():
            lista_equipamentos.controls.append(
                ft.Text(f'{eq["marca"]} {eq["modelo"]}  -  {eq["numero_serie"]}',
                        size=13, color=COR_TEXTO_SUAVE)
            )

    def inserir_equipamento_click(e):
        if not campo_id_cliente.value:
            avisar("Indica o ID do cliente.")
            return

        cliente = cliente_repository.procurar_por_id(campo_id_cliente.value)
        if cliente is None:
            avisar("Esse cliente não existe.")
            return

        equipamento = Equipamento(id_cliente=campo_id_cliente.value, tipo=campo_tipo.value,
                                   marca=campo_marca.value, modelo=campo_modelo.value,
                                   numero_serie=campo_serie.value)
        equipamento_repository.inserir(equipamento)

        campo_id_cliente.value = ""
        campo_tipo.value = ""
        campo_marca.value = ""
        campo_modelo.value = ""
        campo_serie.value = ""

        carregar_equipamentos()
        page.update()
        avisar("Equipamento inserido com sucesso.")

    conteudo_equipamentos = ft.Column([
        campo_id_cliente,
        campo_tipo,
        ft.Row([campo_marca, campo_modelo]),
        campo_serie,
        ft.Row([ft.OutlinedButton("Adicionar equipamento",
                                   on_click=inserir_equipamento_click,
                                   style=ft.ButtonStyle(color=COR_PRINCIPAL))],
               alignment=ft.MainAxisAlignment.END),
        lista_equipamentos,
    ], spacing=10)

    # ================= ORDENS DE SERVIÇO =================
    campo_id_equipamento = ft.TextField(label="ID do equipamento", expand=True, dense=True)
    campo_defeito = ft.TextField(label="Defeito relatado", expand=True, dense=True)

    lista_ordens = ft.ListView(spacing=2, height=120)

    def carregar_ordens():
        lista_ordens.controls.clear()
        for o in ordem_servico_repository.listar():
            lista_ordens.controls.append(
                ft.Text(f'{o["cliente_nome"]}  -  {o["status"]}  -  {o["defeito_relatado"]}',
                        size=13, color=COR_TEXTO_SUAVE)
            )

    def inserir_ordem_click(e):
        if not campo_id_equipamento.value or not campo_defeito.value:
            avisar("Preenche o ID do equipamento e o defeito.")
            return

        equipamento = equipamento_repository.procurar_por_id(campo_id_equipamento.value)
        if equipamento is None:
            avisar("Esse equipamento não existe.")
            return

        cliente = cliente_repository.procurar_por_id(equipamento.id_cliente)

        ordem = OrdemServico(cliente=cliente, equipamento=equipamento,
                              defeito_relatado=campo_defeito.value)
        ordem_servico_repository.inserir(ordem)

        campo_id_equipamento.value = ""
        campo_defeito.value = ""

        carregar_ordens()
        page.update()
        avisar("Ordem de serviço criada com sucesso.")

    conteudo_ordens = ft.Column([
        campo_id_equipamento,
        campo_defeito,
        ft.Row([ft.OutlinedButton("Abrir ordem",
                                   on_click=inserir_ordem_click,
                                   style=ft.ButtonStyle(color=COR_PRINCIPAL))],
               alignment=ft.MainAxisAlignment.END),
        lista_ordens,
    ], spacing=10)

    # ================= LAYOUT =================
    page.add(
        ft.Container(height=24),
        ft.Text("TechService", size=26, weight=ft.FontWeight.BOLD, color=COR_TEXTO_TITULO),
        ft.Text("Assistência técnica, sem complicações.", color=COR_TEXTO_SUAVE),
        ft.Container(height=16),
        ft.Row(
            [
                secao("Clientes", conteudo_clientes),
                secao("Equipamentos", conteudo_equipamentos),
                secao("Ordens de Serviço", conteudo_ordens),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START,
            scroll=ft.ScrollMode.AUTO,
        ),
        ft.Container(height=24),
    )

    carregar_clientes()
    carregar_equipamentos()
    carregar_ordens()
    page.update()


if __name__ == "__main__":
    ft.run(main)