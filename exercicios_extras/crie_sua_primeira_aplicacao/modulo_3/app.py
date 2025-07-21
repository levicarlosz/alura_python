numeros = range(10)
nomes = ["Joao", "Maria", "Paula", "Camila"]
anos = [2005, 2025]

def listar_numeros(number_list):
    exibe_titulo(
        "2. Crie uma lista e utilize um loop for para percorrer todos os elementos da lista."
    )
    for numero in number_list:
        print(numero)

def soma_impares(number_list):
    exibe_titulo(
        "3. Utilize um loop for para calcular a soma dos números ímpares de 1 a 10."
    )
    soma = 0
    for numero in number_list:
        if numero % 2 != 0 and numero > 0:
            soma = soma + numero
    print(soma)

def numeros_decrescente(number_list):
    exibe_titulo(
        "4. Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente."
    )

    max = len(number_list) - 1
    for numero in number_list:
        print(number_list[max] + 1)
        max -= 1

def tabuada():
    exibe_titulo(
        "5. Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10."
    )

    numero = int(input("Digite Um Número: "))

    for i in range(10 + 1):
        if i > 0:
            print(f"{numero} X {i} = {numero * i}")

def soma_numeros(number_list):
    exibe_titulo(
        "6. Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções."
    )
    soma = 0
    try:
        for numero in range(len(number_list) + 1):
            soma = soma + numero
        print(soma)
    except:
        print("Algo deu errado!")
    
def media_valores(lista):
    exibe_titulo(
        "7. Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia."
    )
    
    soma = 0
    media = 0
    try:
        for numero in range(len(lista) + 1):
            soma = soma + numero
        if len(lista) == 0:
            print("Lista Vazia!")
            pass
        else:
            media = soma / len(lista)
            print(media)
    except:
        print("Algo deu errado!")
    
def exibe_titulo(text):
    print(f"\n{text}\n")

def main():
    listar_numeros(numeros)
    soma_impares(numeros)
    numeros_decrescente(numeros)
    tabuada()
    soma_numeros(numeros)
    media_valores(numeros)
    print(" ")

if __name__ == "__main__":
    main()
