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

    '''
    Inclui um novo item na lista de itens do pedido.
    Nao deve ser possivel incluir itens duplicados (com o mesmo codigo).
    Retornar o item incluido em caso de sucesso e None em caso
    de item duplicado.
    '''
    def inclui_item_pedido(self, codigo, descricao, preco):
        codigos = [item.codigo for item in self.itens]
        if codigo not in codigos:
            novo_item = ItemPedido(codigo, descricao, preco)
            self.itens.append(novo_item)
            return novo_item
        return None

    '''
    Exclui um item do pedido e retorna o item excluido
    Caso o item nao exista, retorne None
    '''
    def exclui_item_pedido(self, codigo):
        codigos = [item.codigo for item in self.itens]
        if codigo not in codigos:
            return None
        for item in self.itens:
            if item.codigo == codigo:
                self.itens.remove(item)
                return item

    '''
    Deve calcular o valor total do pedido, considerando um custo
    adicional pela distancia e fator por distancia percorrida. 
    O fator da distancia varia de acordo com o tipo de pedido.
    O fator_distancia do TipoPedido deve ser multiplicado pela distancia 
    e acrescido ao valor total dos itens. 
    Por exemplo, se o fator_distancia for 2 e a distancia for 5, 
    o total do pedido deve ser acrescido em 10. 
    Ainda, se o cliente for ClienteFidelidade, deve  diminuir o valor total 
    pelo percentual de desconto armazenado no atributo desconto do ClienteFidelidade. 
    Por exemplo, se o valor de desconto for 0.2 e o pedido custar 10, o desconto deve ser
    de 2 e o valor final 8.
    @return um float correspondente ao total do pedido
    '''
    def calcula_valor_pedido(self, distancia: float):
        valor_total = 0
        for item in self.itens:
            valor_total += item.preco_unitario
        valor_total += self.tipo.fator_distancia * distancia
        if isinstance(self.cliente, ClienteFidelidade):
            desconto = valor_total * self.cliente.desconto
            valor_total -= desconto
        return valor_total


pedido1 = Pedido(1, ClienteFidelidade(1, 0.2,'123','theus','rua','123'), TipoPedido('asdaf', 12))
pedido1.inclui_item_pedido(1, 'Hamburguer', 12)
pedido1.calcula_valor_pedido(5)