class Veiculo:
    def __init__(self, nome, marca, modelo, potencia, combustivel, n_pasageiros):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.combustivel = combustivel
        self.n_pasageiros = n_pasageiros



class Automovel(Veiculo):
    
    def __init__(self, nome, marca, modelo, potencia, combustivel, n_pasageiros, cor):
        self.cor = cor
        super().__init__(nome, marca, modelo, potencia, combustivel, n_pasageiros)

    def acelerar():
        print("Automovel acelerou")
        
class Moto(Automovel):
    print("Automovel")

class Pessoa():
    def __init__(self, nome, sobrenome, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco


class Aluno(Pessoa):
    def __init__(self,nome, sobrenome,endereco, matricula, curso):
        self.matricula = matricula
        self.curso = curso
        super().__init__(nome, sobrenome, endereco)


class Moto(Automovel):
    print("Automovel")


