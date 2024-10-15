class CuentaBancaria:
    def __init__(self, balance=0, archivo=None): # por defecto se crea la instancia de la cuenta con balance cero y con un archivo vacio
        self.balance = balance
        self.archivo = archivo
        self.log_cuenta('Cuenta creada')

    def log_cuenta(self, mensaje):
        if self.archivo:
            with open(self.archivo, "a") as f:
                f.write(f"{mensaje}\n")

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            self.log_cuenta(f"Depositando {monto}. El nuevo balance es {self.balance}")
        return self.balance

    def retirar(self, monto):
        if monto > 0:
            self.balance -= monto
            self.log_cuenta(f"Retirando {monto}. El nuevo balance es {self.balance}")
        return self.balance

    def mostrar_balance(self):
        self.log_cuenta(f"Balance actual es de {self.balance}")
        return self.balance
    
    def transferir(self, monto):
        if self.balance >= monto:
            self.balance = self.balance - monto
            return True # Transferencia exitosa
        else:
            print("Fondos insuficientes.")
            return False  # Transferencia fallida por falta de fondos
