from abc import ABC, abstractmethod
from animal import Animal


class Ave(Animal):
    @abstractmethod
    def __init__(self, tamanho_passo: int, altura_voo: int):
        super().__init__(tamanho_passo)
        self.__altura_voo = altura_voo

    @property
    def altura_voo(self):
        return self.__altura_voo
    
    @altura_voo.setter
    def altura_voo(self, altura_voo: int):
        if isinstance(altura_voo, int):
            self.__altura_voo = altura_voo

    def mover(self):
        return f"{super().mover()} VOANDO"

    def produzir_som(self):
        return f"AVE: {super().produzir_som()}"