from professor import Professor
from aluno import Aluno


alunos = []
professores = []

professor = Professor(1, 'Jean', 'Rua tal', '48 9999')
aluno = Aluno(123, 'Ale', 'Outra Rua', professor)

alunos.append(aluno)
professores.append(professor)

print(professor)
print(professor.nome)

print(aluno.orientador.nome)

'''aluno1 = Aluno(123, 'Ale', 'Outra Rua', 'DAVI VITORINO DA SILVA CTC @TEM.FEIRA ON INSTAGRAM')
print(aluno1.orientador.nome)'''

for professor in professores:
    print(professor.nome,professor.telefone)