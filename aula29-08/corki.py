

class CorkiBobsleigh:
    def __init__(self):
        self.__aviao = True
        self.__bobsleigh = True

    @property
    def aviao(self):
        return self.__aviao
    
    @aviao.setter
    def aviao(self,aviao):
        self.__aviao = aviao

    @property
    def bobsleigh(self):
        return self.__bobsleigh
    
    @bobsleigh.setter
    def bobsleigh(self,bobsleigh):
        self.__bobsleigh = bobsleigh

    def vermelho(self):
        print('Barão Mágico para Barão Vermelho, responda!')
        

corki = CorkiBobsleigh()

print(corki.aviao)
print(corki.bobsleigh)
corki.vermelho()
