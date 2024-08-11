from dados import clientes
from excecoes import *
from json import *

# MÉTODOS DA API
class ClienteApi:
    def find_all(self):
        clientes_json = []

        for c in clientes:
            clientes_json.append(dumps(c.__dict__))

        return clientes_json

    def find_by_id(self, id):
        return dumps(self.__find_by_id(id).__dict__)

    def post(self, cliente):
        clientes.append(cliente)
        return dumps(cliente.__dict__)

    def delete_all(self):
        clientes.clear()
        return 'Todos os clientes deletados'

    def delete_by_id(self, id):
        clientes.remove(self.__find_by_id(id))
        return f'Cliente deletado para id = {id}.'

    def update(self, cliente_atualizado):
        clientes[clientes.index(self.__find_by_id(cliente_atualizado.id))] = cliente_atualizado
        return dumps(cliente_atualizado.__dict__)

    def __find_by_id(self, id):
        """Private find by id but not in JSON"""
        for c in clientes:
            if c.id == id:
                return c

        raise NotFoundException(f'Cliente não encontrado para id = {id}.')


