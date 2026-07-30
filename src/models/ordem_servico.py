class OrdemServico:

    STATUS_VALIDOS = ("ABERTA", "EM_ANDAMENTO", "AGUARDANDO_PECAS", "CONCLUIDA", "CANCELADA")
    PRIORIDADES_VALIDAS = ("BAIXA", "MEDIA", "ALTA", "URGENTE")

    def __init__(self, id_equipamento, defeito_relatado, id_tecnico=None,diagnostico=None, solucao=None, status="ABERTA",
    prioridade="MEDIA", prazo_entrega=None, valor_servico=0.00, valor_pecas=0.00, desconto=0.00,
    observacoes=None):
        self.id_ordem = None
        self.id_equipamento = id_equipamento
        self.id_tecnico = id_tecnico
        self.defeito_relatado = defeito_relatado
        self.diagnostico = diagnostico
        self.solucao = solucao
        self.status = status
        self.prioridade = prioridade
        self.prazo_entrega = prazo_entrega
        self.valor_servico = valor_servico
        self.valor_pecas = valor_pecas
        self.desconto = desconto
        self.valor_total = None  # calculado pela base de dados, só é conhecido depois de gravar/ler
        self.observacoes = observacoes
        self.data_abertura = None
        self.data_conclusao = None

    def mostrar(self):
        print("ID:", self.id_ordem)
        print("Equipamento:", self.id_equipamento)
        print("Técnico:", self.id_tecnico)
        print("Defeito relatado:", self.defeito_relatado)
        print("Diagnóstico:", self.diagnostico)
        print("Solução:", self.solucao)
        print("Status:", self.status)
        print("Prioridade:", self.prioridade)
        print("Prazo de entrega:", self.prazo_entrega)
        print("Valor serviço:", self.valor_servico)
        print("Valor peças:", self.valor_pecas)
        print("Desconto:", self.desconto)
        print("Valor total:", self.valor_total)
        print("Data de abertura:", self.data_abertura)
        print("Data de conclusão:", self.data_conclusao)
        print("Observações:", self.observacoes)