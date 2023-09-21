from professor import Professor


class Aluno:
    def __init__(self, matricula: int, nome: str, endereco: str, orientador: Professor):
        if isinstance(matricula, int) and isinstance(nome, str) \
                and isinstance(endereco, str) and isinstance(orientador, Professor):
            self.__matricula = matricula
            self.__nome = nome
            self.__endereco = endereco
            self.__orientador = orientador
        
    @property
    def matricula(self):
         return self.__matricula
    
    @matricula.setter
    def matricula(self,matricula: int):
         if isinstance(matricula, int):
            self.__matricula = matricula

    @property
    def nome(self):
         return self.__nome
    
    @nome.setter
    def nome(self,nome: str):
         if isinstance(nome, str):
            self.__nome = nome

    @property
    def endereco(self):
         return self.__endereco
    
    @endereco.setter
    def endereco(self,endereco: str):
         if isinstance(endereco, str):
            self.__endereco = endereco

    @property
    def orientador(self):
         return self.__orientador
    
    @orientador.setter
    def orientador(self,orientador: Professor):
         if isinstance(orientador, Professor):
             self.__orientador = orientador
