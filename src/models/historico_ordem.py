class HistoricoOrdem:

    def __init__(self, id_ordem, status_anterior, status_novo,
                 data_alteracao, observacao=None, usuario=None):
        self.id_historico = None
        self.id_ordem = id_ordem
        self.status_anterior = status_anterior
        self.status_novo = status_novo
        self.data_alteracao = data_alteracao
        self.observacao = observacao
        self.usuario = usuario

    def mostrar(self):
        print(self.data_alteracao, "-", self.status_anterior, "->",
              self.status_novo, "-", self.observacao)