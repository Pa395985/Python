class Filme:
    def __init__(self, nome, genero, classificacao, duracao):
        self.nome = input("Digite o nome do filme", nome)
        self.genero = input("Digite o genero do filme" , genero)
        self.classificacao = input("Digite o classificação do filme" , genero)
        self.duracao = input("Digite o duração do filme" , genero)

class Serie(Filme):
    def __init__(self, nome, genero, classificacao, duracao, temporada):
        self.temporada = temporada
        super().__init__(nome, genero, classificacao, duracao)


class Documentario(Filme):
    def __init__(self, nome, genero, classificacao, duracao, tema):
        self.tema = tema
        super().__init__(nome, genero, classificacao, duracao)