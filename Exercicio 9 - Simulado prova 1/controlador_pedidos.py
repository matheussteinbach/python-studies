from pedido_duplicado_exception import PedidoDuplicadoException
from pedido import Pedido


class ControladorPedidos():
    def __init__(self):
        self.__pedidos = []

    @property
    def pedidos(self):
        return self.__pedidos

    def busca_pedido_por_numero(self, numero):
        if isinstance(numero, int):
            for pedido in self.pedidos:
                if numero == pedido.numero:
                    return pedido
            return None

    def incluir_pedido(self, pedido):
        if isinstance(pedido, Pedido):
            numeros_pedidos = [
                pedido.numero for pedido in self.pedidos]
            if pedido.numero not in numeros_pedidos:
                self.__pedidos.append(pedido)
            else:
                raise PedidoDuplicadoException

    def excluir_pedido(self, numero):
        pedido = self.busca_pedido_por_numero(numero)
        if not pedido:
            return None
        self.__pedidos.remove(pedido)
        return pedido

    def calcular_faturamento_pedidos(self, distancia, cpf):
        faturamento = 0
        pedidos_por_cpf = []
        for pedido in self.pedidos:
            if pedido.cliente.cpf == cpf:
                pedidos_por_cpf.append(pedido)
        for pedido in pedidos_por_cpf:
            faturamento += pedido.calcula_valor_pedido(distancia)
        return faturamento
