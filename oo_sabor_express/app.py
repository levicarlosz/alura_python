from models.restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiano")
restaurante_mc_donalds = Restaurante("MC Donalds", "Fast Food")
restaurante_mc_donalds.alternar_estado()

restaurante_pizza.avaliar("Pedro", 5)
restaurante_pizza.avaliar("Camila", 4)
restaurante_pizza.avaliar("Joao", 2)

if __name__ == "__main__":
    Restaurante.listar_restaurantes()
    
