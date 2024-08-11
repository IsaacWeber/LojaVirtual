from classes import *
# Módulo para cadastrar dados como se estivessem registrados no Banco de Dados

## Cadastrando clientes
cliente1 = Cliente('Nicolas', 'Kaleb')
cliente1.id = 1
cliente1.cpf = '001.777.444-32'
cliente1.email = 'nicolas@gmail.com'
cliente1.endereco = 'QNM 840832 RECANTO AZUL CLARO APTO 99999 - GO'

cliente2 = Cliente('Amanda', 'Pereira')
cliente2.id = 2
cliente2.cpf = '984.245.253-52'
cliente2.email = 'amandapereira@gmail.com'
cliente2.endereco = 'AV. RECANTO FELIZ DE GOIÁS CS 07 - DF'

cliente3 = Cliente('John', 'Doe')
cliente3.id = 3
cliente3.cpf = '777.333.111-01'
cliente3.email = 'johndoe@gmail.com'
cliente3.endereco = 'New Wall ST. 300 - NY'

cliente3 = Cliente('John', 'Doe')
cliente3.id = 3
cliente3.cpf = '777.333.111-01'
cliente3.email = 'johndoe@gmail.com'
cliente3.endereco = 'New Wall ST. 300 - NY'

cliente4 = Cliente('Maicon', 'Douglas')
cliente4.id = 4
cliente4.cpf = '021.034.999-14'
cliente4.email = 'maicon@gmail.com'
cliente4.endereco = 'AV. Recanto Das Flores CS 25- GO'

cliente5 = Cliente('Jean', 'Filho')
cliente5.id = 5
cliente5.cpf = '555.210.111-01'
cliente5.email = 'jean@gmail.com'
cliente5.endereco = 'Sol Nascente RUA 77 CS 50 - RR'

clientes = [cliente1, cliente2, cliente3, cliente4, cliente5]
