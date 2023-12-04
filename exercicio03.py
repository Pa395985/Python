class Shape:
    def calcular_area(self):
        pass

class Circulo(Shape):
    PI = 3.14
    def calcular_area(self, r, pi):
        return (r * r * pi)

class Retangulo(Shape):
    def calcular_area(self, b ,h):
        return (b * h)
      


circulo = Circulo()
print(" A area do circulo é: ", circulo.calcular_area(2, 3.14))

retangulo = Retangulo()
print("A area do retangulo é:", retangulo.calcular_area(3, 10))


