import os

restaurantes = []


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

def voltar_menu():
    input("Pressione qualquer tecla para sair: ")
    main()

def exibir_subtitulo(texto:str):
    os.system("cls")
    print(f"{texto} \n")

def cadastrar_restaurante():
    exibir_subtitulo("Cadastre um Novo Restaurante:")
    nome_restaurante = input("Nome do Restaurante: ")
    os.system("cls")
    restaurantes.append(nome_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso \n")
    voltar_menu()


def listar_restaurantes():
    exibir_subtitulo("Restaurantes Cadastrados:")
    for restaurante in restaurantes:
        print(f".{restaurante}")
    
    os.system("cls")
    voltar_menu()

def opcao_invalida():
    os.system("cls")
    print("Opção Inválida! \n")
    voltar_menu()


def escolha_opcoes():
    try:
        opcao_escolhida = int(input("Esolha uma Opção: "))
        print(f"Você escolheu a opção {opcao_escolhida}!")

        match (opcao_escolhida):
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print("3. Ativar Restaurante")
            case 4:
                encerrar()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system("cls")
    titulo()
    menu()
    escolha_opcoes()


if __name__ == "__main__":
    main()
