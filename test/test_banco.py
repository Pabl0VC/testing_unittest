import unittest, os
from src.banco import CuentaBancaria

"""Esta clase prueba diferentes funcionalidades de la clase CuentaBancaria usando unittest."""
class CuentaBancariaTest(unittest.TestCase): # es una buena practica traer el mismo nombre de la clase y finalizar con Test

    def setUp(self): #setUp permite reutilizar variables para aplicar en varios metodos de una misma clase
        self.cuenta = CuentaBancaria(balance=1000, archivo='log_cuenta.txt')

    def tearDown(self): # tearDown es un metodo de unittest, por lo que se debe escribir así
        """tearDown se ejecuta después de cada prueba.
        Si el archivo de log existe, lo elimina para asegurarse de que no quede rastro después de las pruebas."""
        if os.path.exists(self.cuenta.archivo):
            os.remove(self.cuenta.archivo)

    def test_depositar(self):
        """Prueba la funcionalidad de depósito.
        Deposita 500 unidades y verifica que el nuevo balance sea 1500."""
        # cuenta = CuentaBancaria(balance=1000)
        nuevo_balance = self.cuenta.depositar(500)
        #assert nuevo_balance == 1500  # no se ocupa esta forma, es mejor utilizar los metodos de assert de unittest
        self.assertEqual(nuevo_balance, 1500, "El balance no es correcto")

    def test_retirar(self):
        """Prueba la funcionalidad de retiro.
        Retira 500 unidades del balance de 1000 y verifica que el nuevo balance sea 500."""
        # cuenta = CuentaBancaria(balance=1000)
        nuevo_balance = self.cuenta.retirar(500)
        self.assertEqual(nuevo_balance,500,"El balance no es correcto") # Verifica si el nuevo balance es el esperado.
        #assert nuevo_balance == 500

    def test_mostra_balance(self):
        """Prueba la funcionalidad de mostrar_balance.
        Verifica que el balance inicial de la cuenta es 1000."""
        # cuenta = CuentaBancaria(balance=1000)
        self.assertEqual(self.cuenta.mostrar_balance(),1000)
        #assert self.cuenta.mostrar_balance() == 1000
        
    def test_transferir(self):
        """Prueba la funcionalidad de transferencia entre cuentas.
        
        1. Realiza una transferencia de 500 unidades y verifica que sea exitosa.
        2. Verifica que el balance después de la transferencia sea de 500.
        3. Intenta transferir una cantidad mayor a los fondos restantes (501) y verifica que la transferencia falle.
        4. Confirma que el balance no cambia después de una transferencia fallida."""
        # Transferencia exitosa (if)
        exito = self.cuenta.transferir(500)
        self.assertTrue(exito) # Verifica que la transferencia fue exitosa. Valida si se devuelve un True
        self.assertEqual(self.cuenta.mostrar_balance(), 500)  # Verifica que el balance es correcto después de la transferencia.

        ## hasta aqui el nuevo balance es 500

        # Transferencia fallida (fondos insuficientes) (else)
        exito = self.cuenta.transferir(501) # Intenta transferir más de lo que hay disponible (500).
        self.assertFalse(exito) # Verifica que la transferencia falló. Verificamos que exito sea False, lo que indica que la transferencia falló debido a fondos insuficientes.
        self.assertEqual(self.cuenta.mostrar_balance(), 500)  # Confirma que el balance no ha cambiado. El balance no debería cambiar porque no se permitió la transferencia

    def test_log_cuenta(self):
        """Prueba la funcionalidad de creación de log.
        Después de depositar 500 unidades, verifica que se haya creado un archivo de log ('log_cuenta.txt')."""
        self.cuenta.depositar(500)
        self.assertTrue(os.path.exists("log_cuenta.txt")) # Verifica si el archivo de log existe después del depósito.
        #assert os.path.exists("log_cuenta.txt")