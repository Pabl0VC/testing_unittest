class CuentaBancaria:
    def __init__(self, balance=0, archivo=None): # por defecto se crea la instancia de la cuenta con balance cero y con un archivo vacio
        """Inicializa una nueva cuenta bancaria con un balance opcional y un archivo de log opcional.
        - balance: valor inicial del saldo de la cuenta (por defecto es 0).
        - archivo: nombre del archivo para registrar las transacciones (por defecto es None, es decir, sin archivo).
        Se llama al método log_cuenta para registrar que la cuenta ha sido creada."""
        self.balance = balance
        self.archivo = archivo
        self.log_cuenta('Cuenta creada') # Registra en el log que la cuenta ha sido creada.

    def log_cuenta(self, mensaje):
        """Registra un mensaje en el archivo si 'archivo' está definido.
        - mensaje: texto a escribir en el archivo de log."""
        if self.archivo:
            with open(self.archivo, "a") as f: # Abre el archivo en modo "append" para agregar nuevos logs.
                f.write(f"{mensaje}\n") # Escribe el mensaje en el archivo seguido de un salto de línea.

    def depositar(self, monto):
        """Deposita una cantidad en la cuenta bancaria.
        - monto: cantidad a depositar. Si es positivo, se suma al balance.
        Registra la transacción en el log y devuelve el nuevo balance."""
        if monto > 0:
            self.balance += monto # Suma el monto al balance si es mayor que 0.
            self.log_cuenta(f"Depositando {monto}. El nuevo balance es {self.balance}") # Registra la transacción en el log.
        return self.balance

    def retirar(self, monto):
        """Retira una cantidad de la cuenta bancaria.
        - monto: cantidad a retirar. Si es positivo, se resta del balance.
        Registra la transacción en el log y devuelve el nuevo balance."""
        if monto > 0:
            self.balance -= monto
            self.log_cuenta(f"Retirando {monto}. El nuevo balance es {self.balance}")
        return self.balance

    def mostrar_balance(self):
        """Devuelve el balance actual de la cuenta.
        Registra el balance actual en el archivo de log."""
        self.log_cuenta(f"Balance actual es de {self.balance}")
        return self.balance
    
    def transferir(self, monto):
        """Transfiere una cantidad desde la cuenta si el balance es suficiente.
        - monto: cantidad a transferir.
        Si el balance es mayor o igual al monto, se realiza la transferencia y devuelve True.
        Si no hay suficientes fondos, devuelve False y no cambia el balance."""
        if self.balance >= monto:
            self.balance = self.balance - monto
            return True # Transferencia exitosa
        else:
            print("Fondos insuficientes.")
            return False  # Transferencia fallida por falta de fondos
