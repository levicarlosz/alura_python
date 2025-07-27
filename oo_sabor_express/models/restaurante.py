from models.avaliacao import Avaliacao


class Restaurante:
    restaurantes = []
    
    def __init__(self, nome:str, categoria:str): # <- Funçao Construtora
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self.status}" 
    
    def alternar_estado(self):
        self._status = not self._status
    
    @classmethod
    def listar_restaurantes(cls): 
        print(f"{"Nome".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliações".ljust(25)} | {"Status".ljust(25)}")
        for restaurante in Restaurante.restaurantes:
            print( f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo.ljust(25)}")
            
    @property
    def ativo(self):
        return "☑" if self._status else "☐"
    
    def avaliar(self, cliente:str, nota:int):
        try:
            if nota >= 0 and nota <= 5:
                avaliacao = Avaliacao(cliente, nota)
                self._avaliacoes.append(avaliacao)
        except:
            print("Insira uma nota entre 0 e 5")
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return "Não Avaliado"
        else:
            soma_avaliacoes = sum(avaliacao._nota for avaliacao in self._avaliacoes)
            media = round(soma_avaliacoes / len(self._avaliacoes), 1)
            return media

