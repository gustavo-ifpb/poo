class Conta:

    numero = '0000-00'
    saldo = 0

    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Impossível realizar o saque, conta sem fundos!')
    
    def transferencia(self, conta, valor):
        if self.saldo >= valor:
            self.saque(valor)
            conta.deposito(valor)
        else:
            print('Impossível realizar transferencia, conta sem fundos!')

if __name__ == '__main__':
    numeroConta = input('Digite o número da conta: ')
    c1 = Conta(numeroConta)
    c1.deposito(100)

    c2 = Conta('0002-00', 200)
    c2.saque(30)
    c2.deposito(200)

    print(c1.saldo, c2.saldo)
    c1.saque(20)
    print(c1.saldo, c2.saldo)
    c1.transferencia(c2, 50)
    print(c1.saldo, c2.saldo)