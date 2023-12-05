from cliente import Cliente
from login import Login

cadastro_cliente= {}

class Cadastro():
    def __init__(self, nome, endereco, email, senha):
        self.senha = senha
        super().__init__(nome, endereco, email)

    def efetua_cadastro(self):

        
        #cadastro_cliente= {}

        nome = input("Digite seu nome")
        endereco = input("Digite seu endereço")
        email = input("Digite seu email")
        senha = input("Digite sua senha de 4 digitos")

        print(f" Bem-vindo .")
        print(cadastro_cliente[nome,endereco,email,senha])

        """
        cadastro['nome'] = input("Digite seu nome")
        cadastro['endereco'] = input("Digite seu endereço")
        cadastro['email'] = input("Digite seu email")
        cadastro['senha'] = input("Digite sua senha de 4 digitos")"""

        """

        nome = input("Digite seu nome: ")
        endereco = input("Digite seu endereço: ")
        email = input("Digite seu email: ")
        senha = int(int("Digite sua senha de 4 dígitos: "))"""


        print(f" Bem-vindo {nome}.")
        print(f"Seu endereço  {endereco} e email {email} foram cadastrados com sucesso! ")
        print(f"A senha cadastrada é {senha} memorise e não compartilhe esse dado")


    def verefica_Cadastro(self):
        print(" Voce  já possui cadastro?")
        print(" Digite 'S' para sim e 'N' para não ")

        resposta = ""

        if resposta =="S":
            from login import Login
            login1 = Login()
            login1.efetua_login()


        if resposta == "N":
            cadastro = Cadastro()
            cadastro.efetua_cadastro()
            
"""
            email = input("Digite seu email: ")
            senha = int(input("Digite sua senha: "))
            login = Login(email, senha)

            if email == cadastro_cliente[email]:
                if senha == cadastro_cliente[senha]:
                    print("Login efetuada com sucesso!")

                else:
                    print(f"usuario {login,senha} ou senha invalidos" )


            if """

