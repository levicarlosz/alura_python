# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoa = {
    "nome": "Joao Batista",
    "idade": 29,
    "cidade": "Santa Catarina"
}

# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

quadrados = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}

def modificando_dicionario():
    exibe_titulo("2 - Utilizando o dicionário criado no item 1:")
    print(f"""{pessoa}
          
1. Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
2. Adicione um campo de profissão para essa pessoa;
3. Remova um item do dicionário.
          """)
    
    pessoa.update({"idade": 32})
    print(f" 1. {pessoa}")
    
    pessoa.update({"profissao": "Advogado"})
    print(f" 2. {pessoa}")
    
    pessoa.update({"CPF": "999.999.999-99"})
    print(f" 3. {pessoa}")
    
    pessoa.popitem()
    print(f" 3. {pessoa}")

def verifica_chave(chave, dicionario):
    exibe_titulo("4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.")
    
    try:
        if chave in dicionario.keys():
            print("Existe")
        else:
            print("Não Existe")
    except:
        print("Error")

def contar_palavras(frase):
    exibe_titulo("5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.")
    
    frase = frase.lower().strip().replace(",", "").split()
    dicionario = {}
    
    for palavra in frase:
        dicionario.update({palavra: frase.count(palavra)})
    print(dicionario)

def exibe_titulo(texto):
    print(f"{texto}\n")


def main():
    modificando_dicionario()
    print("")
    verifica_chave(5, quadrados)
    print("")
    contar_palavras("Ela correu, correu e correu até não aguentar mais.")


if __name__ == "__main__":
    main()