class ContaBancaria:
    def __init__(self, nome, saldo):
        self.nome = nome
        self._saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return f"Nome: {self.nome} | saldo: R${self._saldo}"
    
    @classmethod
    def ativar_conta(self):
        self._ativo = True
        
        
    
conta1 = ContaBancaria("Anthony", 2000)
conta2 = ContaBancaria("Valbertth", 2500)
print(conta1)
print(conta2)