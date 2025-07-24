class Restaurante:
    nome = str
    categoria = str
    ativo = bool 
    
restaurante_praca = Restaurante()
restaurante_praca.nome = "Praça"

# 1. Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
restaurante_praca.categoria = "Italiana"

# 2. Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
restaurante_praca.nome
# 3. Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
if restaurante_praca.ativo == True:
    print(f"Restauante {restaurante_praca.nome} está Ativo")
else:
    print(f"Restauante {restaurante_praca.nome} está Inativo")
    
# 4. Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = restaurante_praca.categoria
# 5. Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.nome = "Bistrô"
# 6. Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome, restaurante_pizza.categoria = "Pizza Place", "Fast Food"

# 7. Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
print(restaurante_pizza.categoria)
# 8. Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True
# 9. Imprima no console o nome e a categoria da instância restaurante_praca.
print(f"{restaurante_pizza.nome} | {restaurante_pizza.categoria}")
