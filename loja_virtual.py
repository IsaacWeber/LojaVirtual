class Produto:
    def __init__(self, id=-1, nome='', marca='', categoria='', modelo='', cor='', preco=0.0, descricao=''):
        self.id = id
        self.nome = nome
        self.marca = marca
        self.categoria = categoria
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.descricao = descricao

    def __str__(self):
        return f'Produto: (Id: {self.id}, Nome: {self.nome})'

class Cartao:
    def __init__(self, id=-1, nome_cliente='', numero='', cvv=0, validade='', bandeira='', funcao=''):
        self.id = id
        self.nomeCliente = nome_cliente
        self.numero = numero
        self.cvv = cvv
        self.validade = validade
        self.bandeira = bandeira
        self.funcao = funcao

    def __str__(self):
        return f'Cartão: (Id:{self.id}, Cliente: {self.nome_cliente})'

class Cliente:
    def __init__(self, id=-1, nome='', sobrenome='', cpf='', email='', endereco='', membro_desde=''):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.email = email
        self.endereco = endereco
        self.membro_desde = membro_desde

    def __str__(self):
        return f'Cliente: (Id: {self.id}, Nome: {self.nome})'

c = Cliente(2, 'NICOLAS', 'KALEB', '70714132152', 'nicolaspbbr@gmail.com', 'AGUAS LINDAS PEROLA 1', '20/05/2025')
print(f'{c.sobrenome}, {c.cpf}, {c.email}, {c.endereco}, {c.membro_desde}')






