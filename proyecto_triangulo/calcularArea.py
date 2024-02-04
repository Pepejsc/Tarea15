import math

class calcularArea:

    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3


    def calcular_area(self):
        # Implementación para calcular el área del triángulo
        # Usando la fórmula de Herón para calcular el área
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return area