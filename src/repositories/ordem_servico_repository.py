import mysql.connector

from src.database.conexao import conectar
from src.models.ordem_servico import OrdemServico


def inserir(ordem):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """INSERT INTO ordens_servico
             (id_equipamento, id_tecnico, defeito_relatado, diagnostico, solucao,
              status, prioridade, prazo_entrega, valor_servico, valor_pecas, desconto,
              observacoes)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    valores = (ordem.id_equipamento, ordem.id_tecnico, ordem.defeito_relatado,
               ordem.diagnostico, ordem.solucao, ordem.status, ordem.prioridade,
               ordem.prazo_entrega, ordem.valor_servico, ordem.valor_pecas,
               ordem.desconto, ordem.observacoes)

    cursor.execute(sql, valores)
    conexao.commit()

    ordem.id_ordem = cursor.lastrowid

    cursor.close()
    conexao.close()

    return ordem


def procurar_por_id(id_ordem):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = "SELECT * FROM ordens_servico WHERE id_ordem = %s"
    cursor.execute(sql, (id_ordem,))
    linha = cursor.fetchone()

    cursor.close()
    conexao.close()

    if linha is None:
        return None

    return linha_para_ordem(linha)


def listar():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """SELECT * FROM ordens_servico
             WHERE status NOT IN ('CONCLUIDA', 'CANCELADA')
             ORDER BY data_abertura"""
    cursor.execute(sql)
    linhas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return linhas


def listar_por_equipamento(id_equipamento):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = "SELECT * FROM ordens_servico WHERE id_equipamento = %s ORDER BY data_abertura"
    cursor.execute(sql, (id_equipamento,))
    linhas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return linhas


def atualizar_status(id_ordem, novo_status):
    # A própria base de dados (triggers) trata do histórico e da
    # data_conclusao automaticamente. Aqui só mudamos o status.
    if novo_status not in OrdemServico.STATUS_VALIDOS:
        raise ValueError(f"Status inválido: {novo_status!r}")

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = "UPDATE ordens_servico SET status = %s WHERE id_ordem = %s"
        cursor.execute(sql, (novo_status, id_ordem))
        conexao.commit()
    except mysql.connector.errors.DatabaseError as erro:
        # Ex.: tentar reabrir uma ordem já CANCELADA -- bloqueado pelo
        # trigger trg_os_before_update na base de dados.
        conexao.rollback()
        raise ValueError(str(erro)) from erro
    finally:
        cursor.close()
        conexao.close()


def listar_historico(id_ordem):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """SELECT status_anterior, status_novo, observacao, data_alteracao
             FROM historico_ordens_servico
             WHERE id_ordem = %s
             ORDER BY data_alteracao"""
    cursor.execute(sql, (id_ordem,))
    linhas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return linhas


def linha_para_ordem(linha):
    ordem = OrdemServico(
        id_equipamento=linha["id_equipamento"],
        defeito_relatado=linha["defeito_relatado"],
        id_tecnico=linha["id_tecnico"],
        diagnostico=linha["diagnostico"],
        solucao=linha["solucao"],
        status=linha["status"],
        prioridade=linha["prioridade"],
        prazo_entrega=linha["prazo_entrega"],
        valor_servico=linha["valor_servico"],
        valor_pecas=linha["valor_pecas"],
        desconto=linha["desconto"],
        observacoes=linha["observacoes"]
    )
    ordem.id_ordem = linha["id_ordem"]
    ordem.valor_total = linha["valor_total"]
    ordem.data_abertura = linha["data_abertura"]
    ordem.data_conclusao = linha["data_conclusao"]
    return ordem