class Clube:
    def __init__(self, nome):
        self.nome = nome
        self.socios = []

    def inclui_socio(self, socio):
        self.socios.append(socio)

class Socio:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


# Agregação - Objetos de uma Classe são formados por objetos de outra
# Clube agregação de Sócio / Todo e Parte
# Agregação - Associação com mais dependência

'''clube = Clube('Sport Clube Corinthians Paulista')
socio1 = Socio('Jean','48 9999')
socio2 = Socio('Pedro','48 9998')

clube.inclui_socio(socio1.nome)
clube.inclui_socio(socio2.nome)

for socio in clube.socios:
    print('Sócio:', socio)'''

# Composição
# Todo parte mais forte, não existe parte fora do todo

class Livro:
    def __init__(self, titulo: str):
        self.titulo = titulo
        self.paginas = []

    def inclui_pagina(self, numero, texto):
        pagina = Pagina(numero, texto)
        self.paginas.append(pagina)

class Pagina:
    def __init__(self, numero, texto):
        self.numero = numero
        self.texto = texto

livro = Livro('A sociedade do anel')

#pagina1 = Pagina(1,'O mundo está mudando...')
#pagina2 = Pagina(2,'Frodo saiu do condado')

livro.inclui_pagina(1,'O mundo está mudando...')
livro.inclui_pagina(2,'Frodo saiu do condado.')

for paginas in livro.paginas:
    print(paginas.texto)

# Pode criar outras paginas com o mesmo conteudo
# Porém, não será a mesma instancia de pagina
