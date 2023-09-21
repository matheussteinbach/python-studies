#Lista de Exercícios 12
#01
'''pessoas = list()
temp = list()
maior = 0
menor = 0

while True:
    temp.append(input('Digite o nome:'))
    temp.append(int(input('Digite a idade:')))
    temp.append(float(input('Digite o peso:')))
    if len(pessoas) == 0:
        maior = temp[2]
        menor = temp[2]
    else:
        if temp[2] > maior:
            maior = temp[2]
        if temp[2] < menor:
            menor = temp[2]
    pessoas.append(temp[:])
    temp.clear()
    resp = input('Deseja cadastrar mais uma pessoa?:').upper()
    if resp == 'N':
        break

print(pessoas)
print('Número de pessoas cadastradas:',len(pessoas))
for i in pessoas:
    if i[2] == maior:
        print('Pessoa(s) mais pesada(s):',i[0], end=' ')
print()
print('Pessoa(s) mais leve(s):', end=' ')
for j in pessoas:
    if j[2] == menor:
        print(j[0], end=' ')
print()
cont = 0
for q in pessoas:
    if q[1] > 20:
        cont += 1
print('Número de pessoas acima de 20 anos:',cont,'pessoa(s)',end=' ')
for q in pessoas:
    if q[1] > 20:
        print('-',q[0],q[1],'anos',end=' ')'''

#02
'''from random import randrange
matriz = list()
temp = list()
ordem = int(input('Digite a ordem da matriz:'))
for i in range(ordem):
    for j in range(ordem):
        temp.append(randrange(0,11))
    matriz.append(temp)
    temp = list()
print(matriz)
linha = int(input('Insira o número da linha desejada:'))
while linha < 0 or linha > 11:
    linha = int(input('Insira um valor válido:'))
operacao = input('Insira a operação desejada(S/M):').upper()
while operacao != 'S' and operacao != 'M':
    operacao = input('Insira uma operação válida:').upper()
soma = 0
for i in matriz[linha]:
    soma += i
if operacao == 'S':
    print(soma)
if operacao == 'M':
    print(soma/ordem)'''
        
#03
'''from random import randrange
matriz = list()
temp = list()
ordem = int(input('Digite a ordem da matriz:'))
for i in range(ordem):
    for j in range(ordem):
        temp.append(randrange(0,11))
    matriz.append(temp)
    temp = list()
print(matriz)
operacao = input('Insira a operação desejada(S/M):').upper()
while operacao != 'S' and operacao != 'M':
    operacao = input('Insira uma operação válida:').upper()
soma = 0
#for i in matriz:
#   soma += i
for i in range(ordem):
    for j in range(ordem):
        
if operacao == 'S':
    print(soma)
if operacao == 'M':
    print(soma/ordem)'''

#04

#05
'''q = int(input('Digite o número de pessoas que foram pesquisadas:'))
lista = [int(x) for x in input('Digite 0 para satisfatório e 1 para não satisfatório:').split()]
while len(lista) != q:
    lista = [int(x) for x in input('Digite apenas para a quantidade equivalente de pesquisados:').split()]
conta0 = 0
conta1 = 0
for i in lista:
    if i == 0:
        conta0 += 1
    else:
        conta1 += 1
if conta0 > conta1:
    print('Y')
else:
    print('N')'''

#06
'''n , r = [int(x) for x in input('Digite a quantidade de nadadores e a quantidade que retornou:').split()]
conjunto1 = set(int(x) for x in input('Digite os voluntarios que retornaram:').split())
conjunto2 = set(int(x) for x in range(1,n+1))
x = conjunto2.difference(conjunto1)
if len(x) > 0 :
    print(x)
else:
    print('*')'''
    
#07
'''p , n = [int(x) for x in input('Digite a altura de pulo e a quantidade de canos:').split()]
canos = [int(x) for x in input('Digite a altura dos canos:').split()]
aux = 0
for i in range(n-1):
    if (canos[i] - canos[i+1]) < p*(-1) or (canos[i] - canos[i+1]) > p:
        print('GAME OVER')
        aux += 1
        break
if aux == 0:
    print('YOU WIN')
else:
    print()'''

#08

#09
'''n = int(input('Digite o número de casos de teste:'))
for i in range(n):
    x = int(input('Digite um número:'))
    soma = 0
    for j in range(1,x):
        if x % j == 0:
            soma += j
    if soma == x:
        print(x,'eh perfeito')
    else:
        print(x,'não eh perfeito')'''

#11
def media(temp):
    soma = 0
    for x in temp[1]:
         soma += x
    media = soma/3
    return media
    
    
alunos = []
temp =[]
while True:
    temp.append(input('Digite o nome do aluno:'))
    temp.append([int(x) for x in input('Digite as 3 notas:').split()])
    media = media(temp)
    temp.append(media)
    alunos.append(temp[:])
    temp.clear()
    resp = input('Deseja cadastrar mais uma pessoa?[S/N]:').upper()
    if resp == 'N':
        break
print(alunos)
    
    