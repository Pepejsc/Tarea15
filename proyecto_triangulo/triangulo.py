import math
import logging

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def tipo_de_triangulo(self):
        # Implementación para determinar el tipo de triángulo
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"
        ...

    def calcular_area(self):
        # Implementación para calcular el área del triángulo
        # Usando la fórmula de Herón para calcular el área
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return area
        ...

if __name__ == "__main__":
    # Configura el sistema de logging
    logging.basicConfig(filename='registro.log', level=logging.ERROR)
    # Ejemplo de uso
    try:
        lado1 = float(input("Ingrese la longitud del primer lado: "))
        lado2 = float(input("Ingrese la longitud del segundo lado: "))
        lado3 = float(input("Ingrese la longitud del tercer lado: "))
        
        t = Triangulo(lado1, lado2, lado3)
        print("Tipo de triángulo:", t.tipo_de_triangulo())
        print("Área del triángulo:", t.calcular_area())
    except ValueError:
        logging.exception("Se ingresó un valor no válido para la longitud del lado.")
    except Exception as e:
        logging.exception("Ocurrió un error inesperado: %s", str(e))
