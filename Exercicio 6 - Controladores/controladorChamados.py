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

    # Retorna os tipos de chamado que foram cadastrados no controlador pelo metodo inclui_tipochamado
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
                self, 
                data: Date, 
                cliente: Cliente, 
                tecnico: Tecnico, 
                titulo: str, 
                descricao: str, 
                prioridade: int, 
                tipo: TipoChamado) -> Chamado:
        chamado = Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
        datas = [chamados.data for chamados in self.chamados]
        clientes = [chamados.cliente for chamados in self.chamados]
        tecnicos = [chamados.tecnico for chamados in self.chamados]
        tipos = [chamados.tipo for chamados in self.chamados]
        if chamado not in datas and clientes and tecnicos and tipos:
            self.__chamados.append(chamado)
            return(chamado)

    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        tipochamado = TipoChamado(codigo, descricao, nome)
        identificadores = [tipos.codigo for tipos in self.tipos_chamados]
        if codigo not in identificadores:
            self.__tipos_chamados.append(tipochamado)
            return tipochamado
