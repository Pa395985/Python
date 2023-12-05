from filme import Filme, Serie, Documentario
from cliente import Cliente
from conta import Conta

cliente_cadastrado = {}

print("#############################")
print("# Bem-vindo(a) ao SenaiFlix #")
print("#        By: IgorLeon       #")
print("#############################")
while True:
    print('Para utilizar nossos serviços, efetue o login.')
    opcao = input("Deseja efetuar o login ou se cadastrar?(l / c): ")
    if opcao == 'l':
        from login import Login
        email = input("Digite o seu email: ")
        senha = input("Digite a sua senha: ")
        cliente_logou = Login(email, senha)
        cliente_logou.efetua_login(email,senha)
    elif opcao == 'c':
        from cadastro import Cadastro
        cliente = Cadastro()
        cliente.efetuar_cadastro()
        print(cliente_cadastrado)

#----------------Inicia Programa----------------

    while True:
        print("----------------------------------------")
        print("-       1 - Alugar Filmes              -")
        print("-       2 - Alugar Série               -")
        print("-       3 - Alugar Documentario        -")
        print("-       4 - Sair                       -")
        print("----------------------------------------")

        opcao = input("Digite a opção desejada: ")

        #----------------Inicia Alugar Filme----------------

        if opcao == '1':
            while True:
                nome= input("Digite o seu nome: ")
                endereco= input("Digite o seu endereço: ") 
                email= input("Digite o seu E-mail: ")
                cliente01 = Cliente(nome, endereco, email)
                print(f"Olá, {nome}. Qual filme deseja alugar?\n")
                break



        #----------------Fecha o Programa----------------
        elif opcao == '4':
            print("Obrigado por utilizar o meu serviço ;-).\n")
            break
        else:
            print("Opção invalida.")
