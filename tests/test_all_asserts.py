import unittest

SERVER = 'Server_A'

"""Este módulo contiene ejemplos del uso de diferentes métodos assert 
proporcionados por unittest para validar condiciones específicas en pruebas unitarias."""
class AllAsserts(unittest.TestCase):
    """Esta clase incluye ejemplos de varios tipos de aserciones para probar el comportamiento del código."""

    def test_assert_Equal(self):
        """assertEqual verifica si dos valores son iguales.
        Si los valores no coinciden, la prueba falla."""
        self.assertEqual(10, 10)  # Verifica que ambos números sean iguales.
        self.assertEqual('hola', 'hola')  # Verifica que ambas cadenas sean iguales.

    def test_assert_true_or_false(self):
        """assertTrue y assertFalse validan si una expresión es verdadera o falsa, respectivamente.
        assertTrue espera que la expresión sea verdadera, y assertFalse espera que sea falsa."""
        self.assertTrue(True)  # Verifica que el valor sea True.
        self.assertFalse(False)  # Verifica que el valor sea False.

    def test_assert_raises(self):
        """assertRaises verifica que se lance una excepción específica dentro de un bloque de código.
        Aquí se utiliza el bloque 'with' para manejar correctamente el contexto de la excepción."""
        with self.assertRaises(ValueError):
            int("No soy un numero")  # Esto debería lanzar un ValueError, ya que no se puede convertir la cadena a un número entero.

    def test_assert_in(self):
        """assertIn verifica que un elemento esté presente en una colección (lista, tupla, etc.).
        assertNotIn verifica que un elemento NO esté presente en una colección."""
        self.assertIn(10, [3, 4, 7, 12, 20, 10, 1])  # Verifica que el número 10 esté en la lista.
        self.assertNotIn(10, [0, 20, 13])  # Verifica que el número 10 NO esté en esta lista.

    def test_assert_dicts(self):
        """assertDictEqual compara si dos diccionarios son iguales."""
        user = {"first_name": "Luis", "last_name": "Barrera"}
        self.assertDictEqual(user, {"first_name": "Luis", "last_name": "Barrera"})  # Verifica que ambos diccionarios sean iguales.

        """assertSetEqual compara si dos conjuntos (sets) son iguales, independientemente del orden."""
        self.assertSetEqual(
            {1, 2, 3}, 
            {2, 1, 3}
        )  # Verifica que ambos sets sean iguales, sin importar el orden.

    """Decoradores para saltar pruebas"""
    @unittest.skip("Trabajo en progreso, será habilitada nuevamente")
    def test_skip(self):
        """Esta prueba se salta siempre debido al decorador @skip.
        El mensaje 'Trabajo en progreso, será habilitada nuevamente' explica la razón del salto.
        En este caso, la prueba no se ejecutará hasta que se retire el decorador o se modifique."""
        self.assertEqual("Hola","chao") # Esta afirmación no se evaluará porque la prueba está saltada.

    @unittest.skipIf(SERVER == 'Server_A',"Saltado porque no estamos en el servidor correspondiente")
    def test_skip_if(self):
        """Esta prueba se salta condicionalmente si la variable SERVER es 'Server_A'.
        @skipIf verifica una condición antes de ejecutar la prueba y la salta si la condición es verdadera.
        El mensaje 'Saltado porque no estamos en el servidor correspondiente' especifica el motivo.
        Si la condición es falsa, la prueba se ejecuta normalmente."""
        self.assertEqual(100,100) # Si no se salta, esta afirmación se evaluará normalmente.
