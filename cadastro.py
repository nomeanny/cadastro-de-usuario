#Lista par armazenar os cadastros
cadastros = []

def cadastraar_usuario(nome, idade, email):
    """Cadastre um novo usuário."""
    usuario = {
        'nome': nome,
        'idade': idade,
        'email': email
    }
    cadastros.append(usuario)
    print(f"Usuario {nome} Cadastrado com sucesso")

def exibir_cadastrado():
    """Exibe todos os usuários cadastrados"""
    if not cadastros:
        print("Nenhum usuario cadastrado")
        return
    
    print("Usuario cadastrados:")
    for i, usuario in enumerate(cadastros, start=1):
        print(f"{i}. Nome: {usuario['nome']}, Idade: {usuario['idade']}, E-mail: {usuario['email']} ")

def main():
    """Função principal que ontrole o fluxo do programa"""
    while True:
        print("\nMenu:")
        print("1. Cadastrar usuario")
        print("2. Exibir usuarios")
        print("3. Sair")

        opcao = input("Escolha uma opção (1/2/3): ")

        if opcao == '1':
            nome = input("Digite o nome do usuario: ")
            idade = int(input("Digite a idade do usuario: "))
            email = input("Digite o e-mail do usuario: ")
            cadastraar_usuario(nome, idade, email)
        elif opcao == '2':
            exibir_cadastrado()
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

#Executa a função principal
if __name__ == "__main__":
    main()