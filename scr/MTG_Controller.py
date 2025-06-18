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

    def obter_cartas_por_cores(self, cores_desejadas):
        return self.model.buscar_cartas_por_cores(cores_desejadas)
    
    def buscar_cartas_por_nome(self, texto):     # Método do Controller que chama o Model para buscar cartas pelo nome
        return self.model.buscar_cartas_por_nome(texto)

    def obter_carta_por_id(self, id_carta):
        return self.model.obter_carta_por_id(id_carta) #para edição
    
    def atualizar_carta(self, id_carta, nome, tipo, custo, quantidade, cores_ids):
        self.model.atualizar_carta(id_carta, nome, tipo, custo, quantidade, cores_ids)

    def validar_entrada_numerica(self, char, campo):
        return self.model.validar_entrada_numerica(char, campo)