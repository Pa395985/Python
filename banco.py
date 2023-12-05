class Banco():
    def __init__(self,nome,conta, agencia):
        self.nome= nome
        self.nconta = conta
        self.agencia = agencia


    def pagamento(self, conta, valor_aluguel, agencia, saldo):
        # conta = int(input("Digite o número da sua Conta"))
        # agencia = int(input("Digite o número da sua Agência"))
        if saldo >= valor_aluguel:
            return saldo - valor_aluguel
        else:
            print("Saldo insuficiente")

