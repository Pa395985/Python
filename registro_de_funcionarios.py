"""
Crie um sistema de registro de funcionários em uma empresa, onde diferentes tipos de funcionários
têm comportamentos específicos.
Crie uma classe Funcionario gerencia com um método
'Calcular salário'. Após, crie subclases de funcionarios especificos, como funcionario CLT, funcionario
Comissionario, Funcionario Estagiario
"""

"""
Crie um sistema que solicite e guarde os dados numa lista ou dicionario.
Crie as instancias das classes

"""
class Funcionario:
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


    def calcular_salario(self):#classe
        pass
    


class Funcionario_clt(Funcionario):#subclasse
    def calcular_salario(self):
        return "CLT"
    

class Funcionario_comissionado(Funcionario):#subclasse
    def calcular_salario(self):
        return "comissionado"
    
class Funcionario_estagiario(Funcionario):#subclasse
    def calcular_salario(self):
        return "estagiario"
    
funcionario_clt = Funcionario_clt()
funcionario_comissionado = Funcionario_comissionado()
funcionario_estagiario = Funcionario_estagiario()

print(funcionario_clt.calcular_salario())
print(funcionario_comissionado.calcular_salario())
print(funcionario_estagiario.calcular_salario())



Funcionario[]



    

