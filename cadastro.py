
cliente_cadastrado = {}

class Cadastro():
    def ver_cadastro(self):
        while True:
            from login import Login
            opcao = input("Você possui cadastro?(s / n): ")
            if opcao == 's':
                email = input("Digite o seu E-mail: ")
                senha = input("Digite a sua senha: ")
                login = Login(email, senha)
                
            elif opcao == 'n':
                cadastro = Cadastro()
                cadastro.efetuar_cadastro()
                
            else:
                print("Opção inválida.")

    def efetuar_cadastro(self):

        nome = input("Digite seu nome: ")
        endereco = input("Digite seu endereço: ")
        email = input("Digite seu email: ")
        senha = input("Digite a sua senha: ")

        cliente_cadastrado = {'Nome': nome, 'Endereço': endereco, 'E-mail': email, 'Senha': senha}

        print(f"Bem-vindo(a) {nome}.")
        print(f"Seu endereço {endereco} e e-mail {email} foram cadastrados com sucesso.")
        print(f"Sua senha {senha} foi cadastrada com sucesso.\n")
        return cliente_cadastrado
