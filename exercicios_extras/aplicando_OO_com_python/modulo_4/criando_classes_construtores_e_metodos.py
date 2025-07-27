# 1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros
#    titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    livros = []
    def __init__(self, titulo:str, autor:str, ano_publicacao:int):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponibilidade = True
        Livro.livros.append(self)
        

    # 2. Na classe Livro, adicione um método especial __str__ que retorna uma mensagem formatada
    #    com o título, autor e ano de publicação do livro.
    #    Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        return f"{self._titulo} por {self._autor} lançado em {self._ano_publicacao}"
    
    
    def emprestar(self):
        self._disponibilidade = not self._disponibilidade
        return self._disponibilidade
    
    @property
    def disponibilidade(self):
        return "Disponivel" if self._disponibilidade == True else "Indisponivel"
    # 4. Adicione um método estático chamado verificar_disponibilidade à classe Livro
    # que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

    
    @classmethod
    def verificar_disponibilidade(cls, ano:int):
        disponiveis = [
            livro for livro in cls.livros
            if livro._ano_publicacao == ano and livro._disponibilidade
        ]
        return disponiveis



# 3. Adicione um método de instância chamado emprestar à classe Livro que define
#    o atributo disponivel como False.
#    Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.


