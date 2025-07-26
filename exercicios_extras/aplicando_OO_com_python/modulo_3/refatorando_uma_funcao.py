# Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão.
# Adicione um método especial __str__ para imprimir uma representação em string da pessoa.
# Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano.
# Por fim, adicione uma propriedade chamada saudacao que retorna uma
# mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa:
    def __init__(self, nome:str, idade:int, profissao:str):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissao
        
    def __str__(self):
        return f"{self._nome} tem {self._idade} anos e trabalha com {self._profissao}"
        
    def aniversario(self):
        self._idade += 1
    
    @property 
    def saudacao(self):
        return f"Olá eu me chamo {self._nome} e trabalho no cargo de {self._profissao}"
        
joao = Pessoa("Joao", 29, "Analista Fiscal")

print(joao.saudacao)