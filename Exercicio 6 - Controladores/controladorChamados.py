from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []
        self.__tipos_chamados = []

    @property
    def chamados(self) -> list:
        return self.__chamados

    @property
    def tipos_chamados(self):
        return self.__tipos_chamados

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        chamados_por_tipo = 0
        for chamado in self.__chamados:
            if chamado.tipo == tipo:
                chamados_por_tipo += 1
        return chamados_por_tipo

    def inclui_chamado(
            self, data: Date, cliente: Cliente, tecnico: Tecnico,
            titulo: str, descricao: str, prioridade: int,
            tipo: TipoChamado) -> Chamado:
        if isinstance(cliente, Cliente) and isinstance(tecnico, Tecnico) and\
                isinstance(tipo, TipoChamado):
            novo_chamado = Chamado(
                data, cliente, tecnico, titulo, descricao, prioridade, tipo)
            identificadores = [
                chamado.identificador for chamado in self.chamados]
            if novo_chamado.identificador not in identificadores:
                self.__chamados.append(novo_chamado)

    def inclui_tipochamado(
            self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        tipochamado = TipoChamado(codigo, descricao, nome)
        identificadores = [tipos.codigo for tipos in self.tipos_chamados]
        if codigo not in identificadores:
            self.__tipos_chamados.append(tipochamado)
        return tipochamado
