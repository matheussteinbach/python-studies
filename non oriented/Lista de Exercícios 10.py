#Lista de Exercícios 10

futebol = {'joao','lucas'}
natacao = {'pedro','joao'}
volei = {'ana','lucas'}
basquete = {'maria', 'pedro'}

total = set()

print('Alunos matriculados no futebol:',futebol)
print('Alunos matriculados na natação:',natacao)
print('Alunos matriculados no volei:',volei)
print('Alunos matriculados no basquete:',basquete)
print('===============================================================================')

while True:
    poss = input('Deseja matricular novos alunos?(S/N)').upper()
    if poss == 'N':
        break
    elif poss == 'S':
        mod = int(input('Digite 1 para Futebol, 2 para Natação, 3 para Volêi e 4 para Basquete: '))
        if mod == 1:
            futebol.add(input('Insira o nome do aluno:'))
        elif mod == 2:
            natacao.add(input('Insira o nome do aluno:'))
        elif mod == 3:
            volei.add(input('Insira o nome do aluno:'))
        elif mod == 4:
            basquete.add(input('Insira o nome do aluno:'))
        else:
            mod = int(input('Valor Inválido. Digite novamente:'))
    elif poss != 'S' or poss != 'N':
        poss = input('Resposta inválida.Digite novamente(S/N):').upper()
print('===============================================================================')
print('Atualização:')
print('Alunos matriculados no futebol:',futebol)
print('Alunos matriculados na natação:',natacao)
print('Alunos matriculados no volei:',volei)
print('Alunos matriculados no basquete:',basquete)
print('===============================================================================')

for a in futebol.intersection(natacao):
        total.add(a)
for b in futebol.intersection(volei):
     total.add(b)
for c in futebol.intersection(basquete):
     total.add(c)
for d in natacao.intersection(volei):
    total.add(d)
for e in natacao.intersection(basquete):
     total.add(e)
for f in volei.intersection(basquete):
    total.add(f)
for g in futebol.intersection(natacao, volei):
    total.add(g)
for h in futebol.intersection(volei, basquete):
    total.add(h)
for i in futebol.intersection(natacao, basquete):
    total.add(i)
for j in natacao.intersection(volei, basquete):
    total.add(j)
for k in futebol.intersection(volei, basquete, natacao):
    total.add(k)

if len(total) > 0 :
    print('Existem alunos em pelo menos 2 modalides.')
    print('Alunos que possuem direito ao desconto:',total)
else:
    print('Não existem alunos em pelo menos 2 modalidades.')

print('===============================================================================')
print('Quantidade de alunos matriculados no futebol:',len(futebol))
print('Quantidade de alunos matriculados na natação:',len(natacao))
print('Quantidade de alunos matriculados no volei:',len(volei))
print('Quantidade de alunos matriculados no basquete:',len(basquete))
print('Número total de alunos:',len(futebol.union(natacao,volei,basquete)))
print('===============================================================================')