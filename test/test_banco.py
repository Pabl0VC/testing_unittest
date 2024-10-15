import unittest, os
from src.banco import CuentaBancaria


class CuentaBancariaTest(unittest.TestCase): # es una buena practica traer el mismo nombre de la clase y finalizar con Test

    def setUp(self): #setUp permite reutilizar variables para aplicar en varios metodos de una misma clase
        self.cuenta = CuentaBancaria(balance=1000, archivo='log_cuenta.txt')

    def tearDown(self): # tearDown es un metodo de unittest, por lo que se debe escribir así
        if os.path.exists(self.cuenta.archivo):
            os.remove(self.cuenta.archivo)

    def test_depositar(self):
        # cuenta = CuentaBancaria(balance=1000)
        nuevo_balance = self.cuenta.depositar(500)
        assert nuevo_balance == 1500

    def test_retirar(self):
        # cuenta = CuentaBancaria(balance=1000)
        nuevo_balance = self.cuenta.retirar(500)
        assert nuevo_balance == 500

    def test_mostra_balance(self):
        # cuenta = CuentaBancaria(balance=1000)
        assert self.cuenta.mostrar_balance() == 1000
        
    def test_transferir(self):
        # Transferencia exitosa (if)
        exito = self.cuenta.transferir(500)
        self.assertTrue(exito) # valida si se devuelve un True
        self.assertEqual(self.cuenta.mostrar_balance(), 500) # verificamos que, después de la transferencia exitosa de 500, el nuevo balance de la cuenta es 500

        ## hasta aqui el nuevo balance es 500
        # Transferencia fallida (fondos insuficientes) (else)
        exito = self.cuenta.transferir(501) # se busca transferir 501 pero no hay fondos
        self.assertFalse(exito) # Verificamos que exito sea False, lo que indica que la transferencia falló debido a fondos insuficientes.
        self.assertEqual(self.cuenta.mostrar_balance(), 500)  # El balance no debería cambiar porque no se permitió la transferencia

    def test_log_cuenta(self):
        self.cuenta.depositar(500)
        assert os.path.exists("log_cuenta.txt")