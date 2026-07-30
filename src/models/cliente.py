class Cliente:

    def __init__(
        self,
        nome,
        email,
        telefone="",
        id_cliente=None,
        status=1
    ):
        self.id_cliente = id_cliente
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.status = status