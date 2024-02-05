import unittest
from calcularArea import calcularArea
from tipoTriangulo import tipoTriangulo
from unittest.mock import patch
from triangulo import Triangulo

class TestCalcularArea(unittest.TestCase):
    def test_calcular_area(self):
        area_calculator = CalcularArea(3, 4, 5)
        self.assertAlmostEqual(area_calculator.calcular_area(), 6.0)

class TestTipoTriangulo(unittest.TestCase):
    def test_tipo_equilatero(self):
        tipo_triangulo = TipoTriangulo(4, 4, 4)
        self.assertEqual(tipo_triangulo.tipo(), "Equilátero")

    def test_tipo_isosceles(self):
        tipo_triangulo = TipoTriangulo(5, 5, 6)
        self.assertEqual(tipo_triangulo.tipo(), "Isósceles")

    def test_tipo_escaleno(self):
        tipo_triangulo = TipoTriangulo(3, 4, 5)
        self.assertEqual(tipo_triangulo.tipo(), "Escaleno")

if _name_ == "_main_":
    unittest.main()