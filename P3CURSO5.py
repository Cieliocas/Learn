class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

class ContaCorrente:
    total_contas_criadas = 0
    taxa_de_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero
        ContaCorrente.taxa_de_operacao = 30/ContaCorrente.total_contas_criadas
        ContaCorrente.total_contas_criadas += 1

    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)

    def sacar(self, valor):
        self.saldo -= valor
    
    def depositar(self, valor):
        self.saldo += valor

conta_corrente = ContaCorrente(None, '00', '01')



# cliente = Cliente('jao', '00033399955', 'engenheiro')
# print (cliente.nome)
# print (cliente.cpf)
# print (cliente.profissao)

