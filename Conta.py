class Conta:
    def __init__(self, titular, numero):
        self.saldo = 0.0
        self.numero = numero
        self.titular = titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("saldo não pode ser negativo")
            return # Interrompe a execução do metodo
        self._saldo = saldo

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("saldo insuficiente")


    def deposita(self, valor):
        self.saldo += valor


    def extrato(self):
        print("Cliente: ", self.titular, " Saldo Atual ", self._saldo)
