class Restaurante:
    restaurantes = []
    
    def __init__(self, nome:str, categoria:str): # <- Funçao Construtora
        self.nome = nome
        self.categoria = categoria
        self.status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self.status}" 
    
    def listar_restaurantes(): 
        for restaurante in Restaurante.restaurantes:
            print( f"{restaurante.nome} | {restaurante.categoria} | {restaurante.status}")
            
        
    
restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiano")
restaurante_mc_donalds = Restaurante("MC Donalds", "Fast Food")

Restaurante.listar_restaurantes()

