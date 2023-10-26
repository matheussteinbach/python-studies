from abstractOnibus import AbstractOnibus
from onibusJahCheioException import OnibusJahCheioException
from onibusJahVazioException import OnibusJahVazioException
from onibusJahLigadoException import OnibusJahLigadoException
from onibusJahDesligadoException import OnibusJahDesligadoException


class Onibus(AbstractOnibus):
    def __init__(self, capacidade: int, total_passageiros: int, ligado: bool):
        self.__capacidade = capacidade
        self.__total_passageiros = total_passageiros
        self.__ligado = ligado

    # OnibusJahLigadoException
    def ligar(self) -> str:
        if self.ligado:
            raise OnibusJahLigadoException
        self.__ligado = True

    # OnibusJahDesligadoException
    def desligar(self) -> str:
        if not self.__ligado:
            raise OnibusJahDesligadoException
        self.__ligado = False

    # OnibusJahCheioException
    def embarca_pessoa(self) -> str:
        if self.__total_passageiros == self.__capacidade:
            raise OnibusJahCheioException
        self.__total_passageiros += 1

    # OnibusJahVazioException
    def desembarca_pessoa(self) -> str:
        if self.__total_passageiros == 0:
            raise OnibusJahVazioException
        self.__total_passageiros -= 1

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @property
    def total_passageiros(self) -> int:
        return self.__total_passageiros

    @property
    def ligado(self) -> bool:
        return self.__ligado

    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade
