"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

class Ordenacao():

    def __init__(self, array_para_ordenar:[]):
        """Recebe o array com o conteudo a ser ordenado"""
        self.array = array_para_ordenar

    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        for i in range(len(self.array)):
            menornum = min(self.array[i:])
            indicemenor = self.array[i:].index(menornum)
            self.array[indicemenor + i] = self.array[i]
            self.array[i] = menornum
            
        return self.array
    
    def toString(self):
        """Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
     """
        arrayform = ','.join([str(w) for w in self.array])
        
        return arrayform
    
array = [int(x) for x in input('').split()]
a1 = Ordenacao(array)
a1.ordena()
print(a1.toString())