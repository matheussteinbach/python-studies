from pedido_duplicado_exception import PedidoDuplicadoException
from pedido import Pedido


class ControladorPedidos():
    def __init__(self):
        self.__pedidos = []

    @property
    def pedidos(self):
        return self.__pedidos

    '''
    Busca pedido pelo numero.
    Se o pedido nao existir, deve retornar None
    Caso contrario, retorna o pedido.
    '''
    def busca_pedido_por_numero(self, numero):
        if isinstance(numero, int):
            for pedido in self.pedidos:
                if numero == pedido.numero:
                    return pedido
            return None

    '''
    Incluir pedido na lista.
    Tratar os casos de instancias incorretas e pedido duplicado.
    Caso o pedido já exista na lista, gerar a excecao: 
    PedidoDuplicadoException
    '''
    def incluir_pedido(self, pedido):
        if isinstance(pedido, Pedido):
            numeros_pedidos = [
                pedido.numero for pedido in self.pedidos]
            if pedido.numero not in numeros_pedidos:
                self.__pedidos.append(pedido)
            else:
                raise PedidoDuplicadoException

    '''
    Exclui pedido pelo numero.
    Se o pedido nao existir, deve retornar None
    Caso contrario, retorna o pedido excluido
    '''
    def excluir_pedido(self, numero):
        pedido = self.busca_pedido_por_numero(numero)
        if pedido == None:
            return None
        self.__pedidos.remove(pedido)
        return pedido

    '''
    Deve calcular o total do faturamento para todos os
    itens pedidos por um CPF. 
    Recebe como parametro:
    distancia: um float que corresponde a distancia percorrida
    cpf: uma string representando o CPF do Cliente a ser faturado
    '''
    def calcular_faturamento_pedidos(self, distancia, cpf):
        faturamento = 0
        pedidos_por_cpf = []
        for pedido in self.pedidos:
            if pedido.cliente.cpf == cpf:
                pedidos_por_cpf.append(pedido)
        for pedido in pedidos_por_cpf:
            faturamento += pedido.calcula_valor_pedido(distancia)
            return faturamento
