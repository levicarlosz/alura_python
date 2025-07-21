import os

restaurantes = [{
    "nome": "Massa Saborosa",
    "categoria": "Italiano",
    "ativo": False
},{
    "nome": "Pizza Suprema",
    "categoria": "Pizza",
    "ativo": True
},{
    "nome": "Cantina",
    "categoria": "Italiano",
    "ativo": False
}]


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
    nome, categoria = map(str, input("Dados do Restaurante: ").split(","))
    
    dados_restaurante = {
        "nome": nome.strip(),
        "categoria": categoria.strip(),
        "ativo": False
    }
    
    os.system("cls")
    restaurantes.append(dados_restaurante)
    print(f"O restaurante {nome} foi cadastrado com sucesso \n")
    voltar_menu()


def listar_restaurantes():
    exibir_subtitulo("Restaurantes Cadastrados:")
    for restaurante in restaurantes:
        nome = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "Ativo" if restaurante["ativo"] == True else "Inativo"
        print(f". {nome} | {categoria} | {ativo}")
    print("")
    voltar_menu()

def opcao_invalida():
    os.system("cls")
    print("Opção Inválida! \n")
    voltar_menu()

def ativar_restaurante():
    exibir_subtitulo("3. Ativar/Inativar Restaurante")

    try:
        nome = input("Digite O Nome Do Restaurante: ")
        for restaurante in restaurantes:
            if nome == restaurante["nome"]:
                estado = restaurante["ativo"]
                if estado == True:
                    restaurante["ativo"] = False
                else:
                    restaurante["ativo"] = True
    except:
        print("Operação inválida!")
        
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
                ativar_restaurante()
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
