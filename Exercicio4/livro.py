from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:
    def __init__(
            self, codigo: int, titulo: str, ano: int, editora: Editora,
            autor: Autor, numero_capitulo: int, titulo_capitulo: str
    ):
        if isinstance(codigo, int) and isinstance(titulo, str) and \
                isinstance(ano, int) and isinstance(editora, Editora) and \
                isinstance(autor, Autor) and \
                isinstance(numero_capitulo, int) and \
                isinstance(titulo_capitulo, str):
            self.__codigo = codigo
            self.__titulo = titulo
            self.__ano = ano
            self.__editora = editora
            self.__autores = [autor]
            self.__capitulos = [Capitulo(numero_capitulo, titulo_capitulo)]

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        if isinstance(titulo, str):
            self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        if isinstance(ano, int):
            self.__ano = ano

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        if isinstance(editora, Editora):
            self.__editora = editora

    @property
    def autores(self):
        return self.__autores

    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor):
            if autor not in self.__autores:
                    self.__autores.append(autor)

    def excluir_autor(self, autor: Autor):
        if isinstance(autor, Autor):
            if autor in self.__autores:
                self.__autores.remove(autor)

    def find_capitulo_by_titulo(self, titulo: str):
        try:
            titulos = [capitulo.titulo for capitulo in self.__capitulos]
            indice_capitulo = titulos.index(titulo)
            return self.__capitulos[indice_capitulo]
        except ValueError:
            return None

    def incluir_capitulo(self, numero: int, titulo: str):
        if isinstance(numero, int) and isinstance(titulo, str) and \
                not isinstance(self.find_capitulo_by_titulo(titulo), Capitulo):
            capitulo = Capitulo(numero, titulo)
            self.__capitulos.append(capitulo)

    def excluir_capitulo(self, titulo: str):
        if isinstance(titulo, str):
            excluir_capitulo = self.find_capitulo_by_titulo(titulo)
            if isinstance(excluir_capitulo, Capitulo):
                self.__capitulos.remove(excluir_capitulo)
