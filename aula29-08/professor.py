

class Professor:
    def __init__(self, id_funcionario: int, nome: str, endereco: str, telefone: str):
        if isinstance(id_funcionario, int) and isinstance(nome, str) \
                and isinstance(endereco, str) and isinstance(telefone, str):
            self.__id_funcionario = id_funcionario
            self.__nome = nome
            self.__endereco = endereco
            self.__telefone = telefone

    @property
    def id_funcionario(self) -> int: #documentacao
        return self.__id_funcionario

    @id_funcionario.setter
    def id_funcionario(self, id_funcionario: int):
        if isinstance(id_funcionario, int):
            self.__id_funcionario = id_funcionario

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: int):
        if isinstance(telefone, int):
            self.__telefone = telefone
