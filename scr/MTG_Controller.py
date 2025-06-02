class Controller:
    def __init__(self, model):
        self.model = model
    
    def adicionar_carta(self, nome, tipo, custo, quantidade, cores_ids):
        #Insere a carta e retorna o id
        id_carta = self.model.adicionar_carta(nome, tipo, custo, quantidade)
        #vincula as cores
        self.model.vincular_cores_a_carta(id_carta, cores_ids)
    

    def obter_cores_disponiveis(self):
        return self.model.buscar_cores()
    
    def obter_cartas_com_cores(self):
        return self.model.buscar_cartas_com_cores()

    def excluir_carta(self, id_carta):
        self.model.excluir_carta(id_carta)
