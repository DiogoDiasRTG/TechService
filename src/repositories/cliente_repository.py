from src.database.conexao import conectar
from src.models.cliente import Cliente


def inserir(cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """INSERT INTO clientes (tipo_cliente, nome, telefone, email, nif)
             VALUES (%s, %s, %s, %s, %s)"""
    valores = (cliente.tipo_cliente, cliente.nome, cliente.telefone,
               cliente.email, cliente.nif)

    cursor.execute(sql, valores)
    conexao.commit()

    cliente.id_cliente = cursor.lastrowid

    cursor.close()
    conexao.close()

    return cliente


def procurar_por_id(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = "SELECT * FROM clientes WHERE id_cliente = %s"
    cursor.execute(sql, (id_cliente,))
    linha = cursor.fetchone()

    cursor.close()
    conexao.close()

    if linha is None:
        return None

    return linha_para_cliente(linha)


def listar():
    # Devolve os clientes ativos, já como dicionários (linhas da base de
    # dados), prontos a usar diretamente: item["nome"], item["email"], etc.
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM clientes WHERE ativo = 1")
    linhas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return linhas


def atualizar(cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """UPDATE clientes
             SET tipo_cliente = %s, nome = %s, telefone = %s,
                 email = %s, nif = %s, ativo = %s
             WHERE id_cliente = %s"""
    valores = (cliente.tipo_cliente, cliente.nome, cliente.telefone,
               cliente.email, cliente.nif, cliente.ativo, cliente.id_cliente)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def remover(id_cliente):
    # Atenção: se o cliente já tiver equipamentos associados, a base
    # de dados recusa o DELETE (chave estrangeira ON DELETE RESTRICT).
    # Nesse caso, usa cliente.desativar() + atualizar() em vez de remover().
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM clientes WHERE id_cliente = %s"
    cursor.execute(sql, (id_cliente,))
    conexao.commit()

    cursor.close()
    conexao.close()


def linha_para_cliente(linha):
    cliente = Cliente(
        nome=linha["nome"],
        telefone=linha["telefone"],
        email=linha["email"],
        nif=linha["nif"],
        tipo_cliente=linha["tipo_cliente"]
    )
    cliente.id_cliente = linha["id_cliente"]
    cliente.ativo = bool(linha["ativo"])
    return cliente
