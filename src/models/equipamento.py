class Equipamento:

    def __init__(self, id_cliente, tipo, marca, modelo, numero_serie,
                 data_compra=None, observacoes=None):
        self.id_equipamento = None
        self.id_cliente = id_cliente
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.data_compra = data_compra
        self.observacoes = observacoes
        self.ativo = True

    def desativar(self):
        self.ativo = False

    def ativar(self):
        self.ativo = True

    def mostrar(self):
        print("ID:", self.id_equipamento)
        print("ID do Cliente:", self.id_cliente)
        print("Tipo:", self.tipo)
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Número de série:", self.numero_serie)
        print("Data da compra:", self.data_compra)
        print("Observações:", self.observacoes)
        print("Ativo:", self.ativo)