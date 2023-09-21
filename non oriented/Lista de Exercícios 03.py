#Lista de Exercícios 03

#01
'''for i in range(2004,2100,4):
    print(i)'''

#02
'''for i in range(1,51) :
    if i%2 == 1 :
        print(i)'''
'''
#03
somanota = 0
for i in range(5):
    nome, nota , mensalidade = input("Insira o seu nome, média geral e mensalidade:").split()
    nota = float(nota)
    mensalidade = float(mensalidade)
    somanota = (somanota) + nota
    print("Soma das notas:",somanota)
    if (i == 0):
        melhornome = nome
        melhornota = nota
        melhormensalidade = mensalidade
    else:
        if (nota > melhornota):
            melhornome = nome
            melhornota = nota
            melhormensalidade = mensalidade
media = somanota / (i + 1)
print("Nome:", melhornome)
print("Mensalidade antiga:", melhormensalidade)
print("Mensalidade nova:", melhormensalidade * 0.7)
print("Média da turma:", somanota / (i + 1))
'''
#04
'''par = 0
impar = 0
for i in range(10):
    n = int(input("Números inteiros: "))
    if n%2 == 0:
        par = par + 1
    else:
        impar=impar+1
print('Quantidade de pares:',par)
print('Quantidade de ímpares:',impar)
#05

numero = int(input('Insira um número para saber se ele é primo:'))
primo = 0
for i in range(1,numero+1):
    if numero%i == 0:
        primo = primo + 1
if primo == 2:
    print('Primo')
else:
    print('Não primo')
  '''
#06

'''numero = int(input('Insira um número para saber se ele é primo:'))
primo = 0
for i in range(1,numero+1):
    if numero%i == 0:
        primo = primo + 1
if primo == 2:
    print('Primo')
else:
    print('Não primo')
    for i in range(1,numero+1):
        if numero%i == 0:
            print(i)'''
            
#07
'''n = int(input("Quantas pessoas serão questionadas?"))
somaidade = 0
for n in range(n) :
    idade = int(input("Insira a idade da pessoa:"))
    somaidade = somaidade + idade
media = somaidade /(n+1)
if media <= 25:
    print("A turma é jovem!")
elif media <= 60:
    print('A turma é adulta.')
else :
    print('A turma é idosa...')'''

#08
'''num1, num2 = input("Insira dois numeros inteiros:").split()
num1 = int(num1)
num2 = int(num2)
soman=0
for i in range(num1+1, num2):
    print(i)
    soman=soman+i
print('A soma dos intervalos é:',soman)'''

#09
'''numb = int(input('Insira o número que deseja saber a tabuada:'))
for i in range (1,11):
    print(numb,' x ', i, '=',numb*i)'''

#10
'''somanota = 0
for i in range(5):
    nome, nota = input("Insira o seu nome e nota:").split()
    nota = float(nota)
    somanota = (somanota) + nota
    if (i == 0):
        melhornome = nome
        melhornota = nota
    else:
        if (nota > melhornota):
            melhornome = nome
            melhornota = nota
media = somanota / (i + 1)
print("Média da turma:", somanota / (i + 1))
print("Melhor aluno:", melhornome)
if melhornota >= 5.75:
    print('Aprovado')
elif melhornota >= 2.75:
    print('Recuperação')
else:
    print('Reprovado')'''
    
#11
'''somanumero = 0
n = int(input("Insira a quantidade numeros inteiros:"))
for n in range (n):
    numero = int(input('Insira um número inteiro:'))
    somanumero = somanumero + numero
    if (n == 0):
        maiornumero = numero
        menornumero = numero
    else:
        if (numero > maiornumero):
            maiornumero = numero
        else:
            if (numero < menornumero) :
                menornumero = numero
print('Média:',somanumero/(n+1))
print('Maior número:',maiornumero)
print('Menor número:',menornumero)'''

#12
somapraia = 0
praia1520 = 0
n = int(input("Insira a quantidade de praias a cadastrar:"))
for n in range (n):
    nomepraia = input('Insira o nome da praia:')
    praia = int(input('Insira a distancia do centro:'))
    somapraia = somapraia + praia
    if (n == 0):
        maiorpraia = praia
        melhorpraia = nomepraia
    else:
        if (praia > maiorpraia):
            maiorpraia = praia
            melhorpraia = nomepraia
        else:
            if 15 <= praia <= 20:
                praia1520 = praia1520 + 1
print('Média:',somapraia/(n+1))
print('Praia mais distante:',melhorpraia)
print('Praias entre 15 e 20km:',praia1520)
