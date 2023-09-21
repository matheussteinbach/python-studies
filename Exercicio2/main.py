from pessoa import Pessoa
from professor import Professor
from aluno import Aluno

alunos = []
professores = []

pessoa1 = Pessoa('Carlos', 'Rua 0')
professor1 = Professor('Jean', 'Rua', 1, '48 9999')
aluno1 = Aluno('Matheus', 'Rua 2', 1, professor1)

print(aluno1.nome)
print(aluno1.orientador.nome)