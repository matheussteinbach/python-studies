from cliente import Cliente
from tipo_pedido import TipoPedido
from item_pedido import ItemPedido
from cliente_fidelidade import ClienteFidelidade


class Pedido():
    def __init__(self, numero: int, cliente: Cliente, tipo: TipoPedido):
        self.__numero = numero
        self.__cliente = cliente
        self.__tipo = tipo
        self.__itens = []

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def tipo(self):
        return self.__tipo

    @property
    def itens(self):
        return self.__itens

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    def inclui_item_pedido(self, codigo, descricao, preco):
        codigos = [item.codigo for item in self.itens]
        if codigo not in codigos:
            novo_item = ItemPedido(codigo, descricao, preco)
            self.itens.append(novo_item)
            return novo_item
        return None

    def exclui_item_pedido(self, codigo):
        codigos = [item.codigo for item in self.itens]
        if codigo not in codigos:
            return None
        for item in self.itens:
            if item.codigo == codigo:
                self.itens.remove(item)
                return item

    def calcula_valor_pedido(self, distancia: float):
        valor_total = 0
        for item in self.itens:
            valor_total += item.preco_unitario
        valor_total += self.tipo.fator_distancia * distancia
        if isinstance(self.cliente, ClienteFidelidade):
            desconto = valor_total * self.cliente.desconto
            valor_total -= desconto
        return valor_total
