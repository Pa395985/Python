
from cadastro import Cadastro
#cadastro_cliente = {}
class Login(Cliente):
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha


    def efetua_login(self, email, senha):
        from cadastro import Cadastro
        cadastro = Cadastro()

        self.email = input("Digite seu email: ")
        self.senha = input("Digite sua senha: ")
        
        if(self.email == cadastro.email):
            if(self.senha == cadastro.senha):
                print("Login efetuado com sucesso")
        else:
            print("E-mail ou senha inválidos")


            #login.email = input("Digite seu email: ")
#login.senha = input("Digite sua senha: ")