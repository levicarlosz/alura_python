class Restaurante:
    restaurantes = []
    
    def __init__(self, nome:str, categoria:str): # <- Funçao Construtora
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self.status}" 
    
    def alternar_estado(self):
        self._status = not self._status
    
    @classmethod
    def listar_restaurantes(cls): 
        print(f"{"Nome".ljust(25)} | {"Categoria".ljust(25)} | {"Status".ljust(25)}")
        for restaurante in Restaurante.restaurantes:
            print( f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)}")
            
    @property
    def ativo(self):
        return "☑" if self._status else "☐"
    

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiano")
restaurante_mc_donalds = Restaurante("MC Donalds", "Fast Food")
restaurante_mc_donalds.alternar_estado()

Restaurante.listar_restaurantes()

