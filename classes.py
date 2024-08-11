class Compra:
    def __init__(self):
        self.id = -1
        self.realizacao = ''
        self.entrega = ''
        self.status = ''
        self.cliente = None
        self.cartao = None
        self.produtos = []

    def __str__(self):
        return f'Compra: (Id: {self.id}, Produtos: {self.produtos}, Status: {self.status})'

class Produto:
    def __init__(self, nome='', preco=0.0):
        self.id = -1
        self.nome = nome
        self.preco = preco
        self.marca = ''
        self.categoria = ''
        self.modelo = ''
        self.cor = ''
        self.descricao = ''
        self.compras = []

    def __str__(self):
        return f'Produto: (Id: {self.id}, Nome: {self.nome})'


class Cartao:
    def __init__(self, numero='', validade='', cvv=0):
        self.id = -1
        self.numero = numero
        self.validade = validade
        self.cvv = cvv
        self.nome_cliente = ''
        self.bandeira = ''
        self.funcao = ''
        self.cliente = None
        self.compras = []

    def __str__(self):
        return f'Cartão: (Id:{self.id}, Cliente: {self.numero})'

class Cliente:
    def __init__(self, nome='', sobrenome=''):
        self.id = -1
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = ''
        self.email = ''
        self.endereco = ''
        self.membro_desde = ''
        self.cartoes = []
        self.compras = []

    def __str__(self):
        return f'Cliente: (Id: {self.id}, Nome: {self.nome} {self.sobrenome})'
