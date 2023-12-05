from filme_series import Filme, Serie, Documentario

from cliente import  Cliente
from login import Login
from conta import Conta
from cadastro import Cadastro, ver


print("####################################")
print("       Bem vindo a SenaiFlix        ")
print("####################################")
    


"""login = Login()

login.efetua_login()
login.email = input("Digite seu email: ")
login.senha = input("Digite sua senha: ")"""

# Chama a classe login e seu metodo para efetuar login
1
clientes = {}

while True:
    print(" Escolha uma opção: ")
    print(" Opção 1. Alugar um filme")
    print(" Opção 2. Alugar um Seirie")
    print(" Opção 3. Alugar um filmes")
    print(" Opção 4. Deletar Títulos")
    print(" Opção 5. Sair")


    opcao = input("")

    if opcao == "4":
        break

    if opcao == "1":
        cadastro = Cadastro()
        cadastro.verefica_Cadastro()
    break



                
    """
    elif opcao == "1":
        print(" Escolha uma opção: ")
        print(" Opção 1. Inserir Filmes")
        print(" Opção 2. Inserir Séries")
        print(" Opção 3. Inserir Documentarios  ")
        print(" Opção 4. Sair")


        opcao = int(input(""))


    if opcao == "4":
        break

    if opcao == "1": """

    """

        nome = input("Digiete seu nome:")
        email = input("Digite seu email:")
        endereco = input("Digite seu endereço:")
        cliente = Cliente(nome, endereco, email)
        print(f"Bem vindo{nome}. ")
    
    if opcao == 1:
        filme = Filme("Matrix ", "Ficção " 18, 180)
        #filme
        """