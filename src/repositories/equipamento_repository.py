from src.database.conexao import conectar
from src.models.equipamento import Equipamento


def inserir(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """INSERT INTO equipamentos
             (id_cliente, tipo, marca, modelo, numero_serie, data_compra, observacoes)
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    valores = (equipamento.id_cliente, equipamento.tipo, equipamento.marca,
               equipamento.modelo, equipamento.numero_serie,
               equipamento.data_compra, equipamento.observacoes)

    cursor.execute(sql, valores)
    conexao.commit()

    equipamento.id_equipamento = cursor.lastrowid

    cursor.close()
    conexao.close()

    return equipamento


def procurar_por_id(id_equipamento):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = "SELECT * FROM equipamentos WHERE id_equipamento = %s"
    cursor.execute(sql, (id_equipamento,))
    linha = cursor.fetchone()

    cursor.close()
    conexao.close()

    if linha is None:
        return None

    return linha_para_equipamento(linha)


def listar():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM equipamentos WHERE ativo = 1")
    linhas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return linhas


def listar_por_cliente(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = "SELECT * FROM equipamentos WHERE id_cliente = %s AND ativo = 1"
    cursor.execute(sql, (id_cliente,))
    linhas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return linhas


def atualizar(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """UPDATE equipamentos
             SET id_cliente = %s, tipo = %s, marca = %s, modelo = %s,
                 numero_serie = %s, data_compra = %s, observacoes = %s, ativo = %s
             WHERE id_equipamento = %s"""
    valores = (equipamento.id_cliente, equipamento.tipo, equipamento.marca,
               equipamento.modelo, equipamento.numero_serie,
               equipamento.data_compra, equipamento.observacoes,
               equipamento.ativo, equipamento.id_equipamento)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def remover(id_equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM equipamentos WHERE id_equipamento = %s"
    cursor.execute(sql, (id_equipamento,))
    conexao.commit()

    cursor.close()
    conexao.close()


def linha_para_equipamento(linha):
    equipamento = Equipamento(
        id_cliente=linha["id_cliente"],
        tipo=linha["tipo"],
        marca=linha["marca"],
        modelo=linha["modelo"],
        numero_serie=linha["numero_serie"],
        data_compra=linha["data_compra"],
        observacoes=linha["observacoes"]
    )
    equipamento.id_equipamento = linha["id_equipamento"]
    equipamento.ativo = bool(linha["ativo"])
    return equipamento