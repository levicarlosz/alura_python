def numeroPar():
    print("1. Exercício")

    numero = int(input("Digite um numero: "))

    if numero % 2 == 0:
        print(" Número é Par")
    else:
        print(" Número é Impar")


def classificar_idade():
    print("2. Exercício")

    idade = int(input("Digite Sua Idade:"))
    if idade > 0 and idade <= 12:
        print("Você é uma criança")
    elif idade >= 13 and idade < 18:
        print("Você é um adolescente")
    else:
        print("Você é Adulto")


def login():
    print("3. Exercício")

    senha_padrao, usuario_padrao = "12345", "admin"
    usuario, senha = input("digite seu usuario: "), input("digite sua senha: ")

    if usuario == usuario_padrao and senha == senha_padrao:
        print(f"bem-vindo {usuario}")
    else:
        print("Ops credenciais inválidas")


def coordenadas():
    x, y = map(float, input().split())
    
    if x > 0 and y > 0:
        print("O ponto está no Primeiro Quadrante.")
    elif x < 0 and y > 0:
        print("O ponto está no Segundo Quadrante.")
    elif x < 0 and y < 0:
        print("O ponto está no Terceiro Quadrante.")
    elif x > 0 and y < 0:
        print("O ponto está no Quarto Quadrante.")
    else:
        print("O ponto está localizado no eixo ou na origem.")


def main():
    numeroPar()
    classificar_idade()
    login()
    coordenadas()


if __name__ == "__main__":
    main()
