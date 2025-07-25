# 1. Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano.
# Crie uma instância dessa classe e atribua valores aos seus atributos.


class Carro:
    def __init__(self, modelo: str, cor: str, ano: int):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano


tesla_model_3 = Carro("Tesla Model 3", "Preta", "2022")

# 2. Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos.
# Instancie um restaurante e atribua valores aos seus atributos.


class Restaurante:
    def __init__(
        self, nome: str, categoria: str, ativo: bool, local: str, preco_medio: float
    ):
        self.nome, self.categoria, self.ativo, self.local, self.preco_medio = (
            nome,
            categoria,
            ativo,
            local,
            preco_medio,
        )
    # Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância,
    # seja exibida uma mensagem formatada com o nome e a categoria.
    # Exiba essa mensagem para uma instância de restaurante.

    def __str__(self):
        return f"{self.nome}, {self.categoria}, {self.ativo}, {self.local}, {self.preco_medio}"


brasa_forte = Restaurante("Brasa Forte", "Rodizios", True, "Rua X Avenida Y", 89.90)

print(brasa_forte)


# Crie uma classe chamada Cliente e pense em 4 atributos.
# Em seguida, instancie 3 objetos desta classe e atribua valores aos seus
# atributos através de um método construtor.

class Cliente:
    clientes = []
    def __init__(self, nome:str, sobrenome:str, numero_pedido:int, metodo_pagamento:str):
        self.nome, self.sobrenome, self.numero_pedido, self.metodo_pagamento = nome, sobrenome, numero_pedido, metodo_pagamento
        Cliente.clientes.append(self)
        
    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f"{cliente.nome}, {cliente.sobrenome}, {cliente.numero_pedido}, {cliente.metodo_pagamento}")
            
cliente_pedro = Cliente("Pedro", "Batista", 56, "PIX")
cliente_joana = Cliente("Joana", "Ribas", 33, "Dinheiro")
cliete_matheus = Cliente("Matheus", "Carvalho", 77, "Cartão de Crédito")

Cliente.listar_clientes()