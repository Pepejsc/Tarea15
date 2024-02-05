import math
import logging
from calcularArea import calcularArea
from tipoTriangulo import tipoTriangulo

class Triangulo:
    def __init__(self):
        # Código del constructor vacío
        pass

if __name__ == "__main__":
    # Configura el sistema de logging
    logging.basicConfig(filename='registro.log', level=logging.ERROR)
    # Ejemplo de uso
    try:
        lado1 = float(input("Ingrese la longitud del primer lado: "))
        lado2 = float(input("Ingrese la longitud del segundo lado: "))
        lado3 = float(input("Ingrese la longitud del tercer lado: "))
        
        tipo_triangulo = tipoTriangulo(lado1, lado2, lado3)
        calcular_area = calcularArea(lado1, lado2, lado3)

        print("Tipo de triángulo:", tipo_triangulo.tipo())
        print("Área del triángulo:", calcular_area.calcular_area())

    except ValueError:
        logging.exception("Se ingresó un valor no válido para la longitud del lado.")
    except Exception as e:
        logging.exception("Ocurrió un error inesperado: %s", str(e))
