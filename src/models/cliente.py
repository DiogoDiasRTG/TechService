class Cliente:

    def __init__(self, nome, telefone, email, nif, tipo_cliente="FISICA"):
        self.id_cliente = None
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.nif = nif
        self.tipo_cliente = tipo_cliente
        self.ativo = True

    def desativar(self):
        self.ativo = False

    def ativar(self):
        self.ativo = True

    def mostrar(self):
        print("ID:", self.id_cliente)
        print("Nome:", self.nome)
        print("Telefone:", self.telefone)
        print("Email:", self.email)
        print("NIF:", self.nif)
        print("Tipo:", self.tipo_cliente)
        print("Ativo:", self.ativo)
