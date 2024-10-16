import unittest
from tests.test_banco import CuentaBancariaTest # Importamos la clase de prueba que contiene las pruebas unitarias de la cuenta bancaria.

def cuenta_banco_suite():
    """Esta función crea una suite de pruebas personalizada que agrupa varias pruebas específicas de la clase CuentaBancariaTest.
    
    La suite es una colección de pruebas que se pueden ejecutar juntas. 
    En este caso, se añaden las pruebas 'test_depositar' y 'test_retirar' a la suite."""
    suite = unittest.TestSuite() # Creamos una nueva instancia de TestSuite, que es una colección de pruebas.
    suite.addTest(CuentaBancariaTest("test_depositar")) # Añade la prueba 'test_depositar' a la suite.
    suite.addTest(CuentaBancariaTest("test_retirar")) # Añade la prueba 'test_retirar' a la suite.
    return suite


if __name__ == "__main__":
    # Para ejecurar suites debemos hacerlo con un runner. El runner ejecuta las pruebas y muestra los resultados.
    runner = unittest.TextTestRunner()
    runner.run(cuenta_banco_suite())
    # Se debe correr en este caso con el comando PYTHONPATH=. python3 tests/suites.py