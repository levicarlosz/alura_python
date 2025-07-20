import os

def encerrar():
    os.system("cls")
    print("Finalizado...")

def titulo():
    print(
        """
▒█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ▒█▀▀▀ █░█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
░▀▀▀▄▄ █▄▄█ █▀▀▄ █░░█ █▄▄▀ 　 ▒█▀▀▀ ▄▀▄ █░░█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
▒█▄▄▄█ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀▀ 　 ▒█▄▄▄ ▀░▀ █▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ▀▀▀
      """
    )


def menu():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar Restaurante")
    print("4. Sair \n")


def escolha_opcoes():
    opcao_escolhida = int(input("Esolha uma Opção: "))
    print(f"Você escolheu a opção {opcao_escolhida}!")

    match(opcao_escolhida):
        case 1:
            print("1. Cadastrar Restaurante")
        case 2:
            print("2. Listar Restaurantes")
        case 3:
            print("3. Ativar Restaurante")
        case 4:
            encerrar()
        case _:
            print("Opção Inválida! \n")


def main():
    titulo()
    menu()
    escolha_opcoes()


if __name__ == "__main__":
    main()
