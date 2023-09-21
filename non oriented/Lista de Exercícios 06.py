#Lista de Exercícios 06

#01    
'''def calculosalario(sal,porc):
    novosal = sal * porc
    reajuste = novosal - sal
    percentual = (porc - 1) * 100
    print("Novo salário: {:.2f}".format(novosal))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: {:.0f}".format(percentual),"%")

sal = float(input("Insira seu salário:"))
if sal < 0 :
    print("Salário invalido.")
elif sal <= 400 :
    calculosalario(sal,1.15)  
elif sal <= 800 :
    calculosalario(sal,1.12) 
elif sal <= 1200 :
    calculosalario(sal,1.1) 
elif sal <= 2000 :
    calculosalario(sal,1.07) 
else :
    calculosalario(sal,1.04) '''
    
#02
'''def horario(saida,tempo,fuso):
    chegada = saida + tempo + fuso
    if chegada >= 24:
        print(chegada-24)
    elif chegada < 0:
        print(chegada+24)
    else:
        print(chegada)
saida ,tempo, fuso = [int(x) for x in input('Insira o horário de saída, tempo de viagem e o fuso:').split()]
horario(saida,tempo,fuso)'''


#03
'''def ultra(x,z,somax,contador):
    for i in range (x,z):
        somax += i
        contador += 1
        if somax > z:
            print(contador)
            break
        
#    while somax <= z :
#        somax = somax + (x + contador)
#        contador += 1
#    print(contador)
x = int(input('Insira o valor de X:'))
z = int(input('Insira o valor de Z:'))
while x >= z:
    z = int(input('Insira um valor maior que X:'))
ultra(x,z,0,0)'''

#04
'''def quadrante(x,y):
    if x > 0 and y > 0:
        print('Primeiro')
    elif x > 0 and y < 0:
        print('Quarto')
    elif x < 0 and y > 0:
        print('Segundo')
    else:
        print('Terceiro')

while True:
    x,y = [int(x) for x in input('Insira as coordenadas X e Y:').split()]
    if x == 0 or y == 0:
        break
    else:
        quadrante(x,y)'''
#05
'''def elevador(n,c):
    contador = 0
    for i in range(n):
        s,e = [int(x) for x in input('Insira o número de quantos sairam e quantos entraram:').split()]
        contador = contador - s + e
        if contador > c:
            print('S')
            break
    if contador <= c:
        print('N')

n ,c = [int(x) for x in input('Insira o número de leituras e a capacidade máxima do elevador:').split()]
elevador(n,c)'''

#06
'''def colchao(altc,largc,compc,altp, largp):
    if altc > largp :
        colchao = 'N'
    elif altc < largp and largc <= altp or compc <= altp :
        colchao = 'S'
    else:
        colchao = 'N'
    return colchao

altc , largc , compc = [int(x) for x in input("Insira a altura ,largura e comprimento do colchão:").split()]
altp, largp = [int(x) for x in input("Insira a altura e a largura da porta:").split()]
colchao = colchao(altc , largc , compc, altp, largp)
if colchao == 'N':
    print('Você deverá procurar um novo colchão.')
if colchao == 'S':
    print('Parabéns! O colchão é do tamanho adequado!')'''

#07
'''def calculo():
    somanota = 0
    for i in range(5):
        nota = float(input("Insira a nota do aluno:"))
        somanota = (somanota) + nota
        if (i == 0):
            melhornota = nota
        else:
            if (nota > melhornota):
                melhornota = nota
    media = somanota / 5
    return media,melhornota

media, melhornota = calculo()
print("Média da turma:", media)
print("Melhor nota:", melhornota)
if melhornota >= 5.75:
    print('Aprovado')
elif melhornota >= 2.75:
    print('Recuperação')
else:
    print('Reprovado')'''

#08
'''def descobrepar(numero):
    paridade = ''
    if numero%2 == 0:
        paridade = 'Par'
    else:
        paridade = 'Impar'
    return paridade

impar = 0
par = 0
for i in range(10):
    numero = int(input('Insira um número inteiro:'))
    paridade = descobrepar(numero)
    print(paridade)
    if paridade == 'Par':
        par += 1
    else:
        impar += 1
print('Número total de pares:',par, end=' ')
print('e impares:',impar)'''

#09
'''def primos(intervalo1,intervalo2):
    primo = 0
    contador = 0
    for i in range(intervalo1,intervalo2+1):
        restos = 0
        for j in range(2,i):
            if (i%j==0):
                restos += 1
                break
        if restos == 0 :
            primo = i
            contador += 1
            print(primo,end= ' ')
    return contador
        

intervalo1,intervalo2 = [int(x) for x in input('Insira o intervalo:').split()]
contador = primos(intervalo1,intervalo2)
print('Numero total de primos:',contador)'''


#10
'''def verificacao(idade):
    verifi = ''
    if idade < 0:
        verifi = 'Parar'
    return verifi


somaidade = 0
contador = 0
while True:
    idade = int(input('Insira as idades:'))
    verifi = verificacao(idade)
    if verifi == '':
        contador += 1
        somaidade += idade
    else:
        break
    
print('Média das idades:',somaidade/contador)'''

#11
'''def positividade(numero):
    positivo = ''
    if numero > 0:
        positivo = 'S'
    return positivo


contador = 0
soma = 0
for i in range(6):
    numero = float(input('Insira um valor:'))
    positivo = positividade(numero)
    if positivo == 'S':
        contador += 1
        soma += numero
        
print(contador,'valores positivos')
print(soma/contador)'''
        
#12
'''def contador(inicio,fim,passo):
    if passo > 0:
        for i in range(inicio,fim+1,passo):
            print(i,end=' ')
    else:
        for i in range(inicio,fim-1,passo):
            print(i,end=' ')

inicio,fim ,passo = [int(x) for x in input('Digite o inicio, fim e passo do contador:').split()]
contador(inicio,fim,passo)'''

#13
def area(largura, comprimento):
    print(largura*comprimento)
    
largura, comprimento = [int(x) for x in input('Digite a largura e o comprimento do terreno:').split()]
area(largura,comprimento)
