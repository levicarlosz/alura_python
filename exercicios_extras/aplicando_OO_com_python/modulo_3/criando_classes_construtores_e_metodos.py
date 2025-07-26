
# 1. Crie uma classe chamada ContaBancaria com um
# construtor que aceita os parâmetros titular e saldo.
# Inicie o atributo ativo como False por padrão.
class ContaBancaria:
    def __init__(self, titular:str, saldo:int):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False
        
        
    # 2. Na classe ContaBancaria, adicione um método especial __str__
    # que retorna uma mensagem formatada com o titular e o saldo da conta.
    # Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self):
        return f"titular: {self._titular.ljust(10)} | saldo: {self._saldo}"
    
    # 3. Adicione um método de classe chamado ativar_conta à classe
    # ContaBancaria que define o atributo ativo como True.
    # Crie uma instância da classe, chame o método de classe e
    # imprima o valor de ativo.
    def ativar_conta(self):
        self._ativo = not self._ativo
        return self._ativo
    
    
conta_patty = ContaBancaria("Patty", 400000)
conta_cria = ContaBancaria("Cria", 1518)

print(conta_patty)
print(conta_cria)
print(conta_patty.ativar_conta())
