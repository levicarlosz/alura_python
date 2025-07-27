# 5. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
from criando_classes_construtores_e_metodos import Livro

harry_potter = Livro("Harry Potter e o Cálice de Fogo", "J.K. Rowling", 2000)
guia_lgpd = Livro("Guia Geral Para a Implementação da LGPD", "Daniel Donda", 2000)
codigo_limpo = Livro("Código Limpo", "Robert C. Martin", 2000)
dom_casmurro = Livro("Dom Casmurro", "Machado de Assis", 1899)
o_pequeno_principe = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
codigo_da_vinci = Livro("O Código Da Vinci", "Dan Brown", 2003)

# 6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar
#    e imprima se o livro está disponível ou não após o empréstimo.
guia_lgpd.emprestar()
print(guia_lgpd.disponibilidade)

# 7. No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade
#    para obter a lista de livros disponíveis publicados em um ano específico.

livros_2000 = Livro.verificar_disponibilidade(2000)

for livro in livros_2000:
    print(livro)
