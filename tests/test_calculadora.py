import unittest
from src.calculadora import suma, resta, multiplicacion, division

class CalculadoraTest(unittest.TestCase):
    def test_suma(self):
        assert suma(5,5) == 10

    def test_resta(self):
        assert resta(3,1) == 2

    def test_multiplicacion(self):
        assert multiplicacion(3,1) == 3

    def test_division(self):
            assert division(30,2) == 15

    def test_division_cero(self):
        with self.assertRaises(ZeroDivisionError):
             division(10,0)

if __name__ == "__main__":
    unittest.main()