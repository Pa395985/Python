class Conta:
    def __init__(self, nome, conta, agencia):
        self.nome = nome
        self.conta = conta
        self.agencia = agencia

    def pagamento(self, saldo, valor_aluguel):
        #conta = int(input("Digite o número da sua Conta: ")) #Aguardando aprender sobre Banco de Dados
        #agencia = int(input("Digite o número da sua Agencia: ")) #Aguardando aprender sobre Banco de Dados
        if saldo < valor_aluguel:
            print("Saldo insuficiente.")
        else:
            return saldo - valor_aluguel
