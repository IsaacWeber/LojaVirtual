from api import ClienteApi
from classes import Cliente
from dados import clientes

# CLIENTE CRUD
cliente_api = ClienteApi()

## GET: find all
clientes_json = cliente_api.find_all()
for cjson in clientes_json:
   print(cjson)

## GET: find by id
# cliente = cliente_api.find_by_id(3)
# print(cliente)

## POST: post
# cliente = Cliente('Maradona', 'Marques')
# cliente.id = 6
# print(cliente_api.post(cliente))

## DELETE: delete by id
#print(cliente_api.delete_by_id(2))

## DELETE: delete all
# print(cliente_api.delete_all())

## UPDATE: update
# c = clientes[0]
#
# c.nome = 'jackson'
# c.sobrenome = 'mariano'
# c.cpf = '782.234.324-62'
# c.email = 'jacksonmariano@gmail.com'
# c.endereco = 'Rua 10, Casa 05 Lago Azul - GO'
#
# print(cliente_api.update(c))