class Animal:
    def emitir_son(self):
        pass
    


class Cachorro:
    def emitir_son(self):
        return "Au au"


class Gato:
    def emitir_son(self):
        return "Miau"


cachorro = Cachorro()
gato = Gato()


print(cachorro.emitir_son())
print(gato.emitir_son())

    