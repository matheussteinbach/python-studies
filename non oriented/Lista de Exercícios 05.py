#Lista de Exercícios 05
 
#01
'''while True:
    x,y = input("Digite um par de números inteiros:").split()
    x = int(x)
    y = int(y)
    if x > y:
        print("Decrescente.")
    elif x < y:
        print("Crescente.")
    else:
        break'''

#02
'''n = int(input('Insira o número de testes:'))
for n in range (n):
    x, y = input('Insira um par de números inteiros:').split()
    x = int(x)
    y = int(y)
    somaimpar = 0
    if x > y :
        aux = x
        x = y
        y = aux
    for i in range(x+1,y):
        if i%2 != 0:
            somaimpar += i
    print(somaimpar)'''

#03
'''valor = float(input('Insira o valor:'))
n100 = valor/100
n50 = (valor%100)/50
n20 = ((valor%100)%50)/20
n10 = (((valor%100)%50)%20)/10
n5 = ((((valor%100)%50)%20)%10)/5
n2 = (((((valor%100)%50)%20)%10)%5)/2
m1 = ((((((valor%100)%50)%20)%10)%5)%2)/1
m50 = (((((((valor%100)%50)%20)%10)%5)%2)%1)/0.5
m25 = ((((((((valor%100)%50)%20)%10)%5)%2)%1)%0.5)/0.25
m10 = (((((((((valor%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25)/0.1
m5 = ((((((((((valor%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25)%0.1)/0.05
m1 = (((((((((((valor%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25)%0.1)%0.05)/0.01

print("NOTAS:")
print(int(n100),"nota(s) de R$ 100.00")
print(int(n50),"nota(s) de R$ 50.00")
print(int(n20),"nota(s) de R$ 20.00")
print(int(n10),"nota(s) de R$ 10.00")
print(int(n5),"nota(s) de R$ 5.00")
print(int(n2),"nota(s) de R$ 2.00")
print("MOEDAS:")
print(int(m1),"moeda(s) de R$ 1.00")
print(int(m50),"moeda(s) de R$ 0.50")
print(int(m25),"moeda(s) de R$ 0.25")
print(int(m10),"moeda(s) de R$ 0.10")
print(int(m5),"moeda(s) de R$ 0.05")
print(int(m1),"moeda(s) de R$ 0.01")'''

#04
'''dist, vf, vg = input('Insira a distancia entre os barcos, a velocidade do fugitivo e a da guarda:').split()
dist = int(dist)
vf = int(vf)
vg = int(vg)
distf = 12
distg= ((dist**2) + (distf**2))**0.5
tempof = distf/vf
tempog = distg/vg
if tempog <= tempof:
    print('S')
else:
    print('N')'''


#05
'''from math import ceil

x, y = input('Insira o tempo em segundos do piloto mais rápido e do mais lento:').split()
x = int(x)
y = int(y)
while not(1 <= x <= 10000):
    x = int(input('Digite novamento o tempo do piloto mais rápido:'))
while not(x < y < 10000):
    y = int(input('Digite novamento o tempo do piloto mais lento:'))
    
diferenca = y - x
calc = ceil(y/diferenca)
print(calc)'''

#06
'''somanota = 0
melhornota = 0
piornota = 0
for i in range(5):
    nota = float(input("Insira a nota:"))
    somanota += nota
    if (i == 0):
        melhornota = nota
        piornota = nota
    elif (nota >= melhornota):
        melhornota = nota
    elif (nota <= piornota):
        piornota = nota
print("{:.1f}".format(somanota - (melhornota + piornota)))'''

#07
'''teste = 0
while True:
    n = int(input('Insira o número de depósitos:'))
    if n == 0:
        break
    diferenca = 0
    teste += 1
    print("Teste",teste)
    for i in range (n):
        j,z = input('Informe o valor do depósito para Joãozinho e Zézinho:').split()
        j = int(j)
        z = int(z)
        diferenca = diferenca + (j - z)
        print(diferenca)'''

#08
'''teste = 0
while True:
    valor = int(input('Insira o valor desejado:'))
    if valor == 0:
        break
    teste += 1
    print('Teste',teste)
    n50 = valor/50
    n10 = (valor%50)/10
    n5 = ((valor%50)%10)/5
    n1 = (((valor%50)%10)%5)/1
    print(int(n50),int(n10),int(n5),int(n1))'''

#09 lista

#10
'''x = int(input('Insira o valor de X:'))
z = int(input('Insira o valor de Z:'))
somax = 0
contador = 0
while x >= z:
    z = int(input('Insira um valor maior que X:'))
#while somax <= z :
#    somax = somax + (x + contador)
#    contador += 1
print(contador)
for i in range (x,z):
    somax += i
    contador += 1
    if somax > z:
        break
print(contador)'''

#11


#12
'''p , r = input('Insira os valores de P e R:').split()
p = int(p)
r = int(r)

if p == 0:
    print('C')
else:
    if r == 0:
        print('B')
    else:
        print('A')'''



#13
'''copoquebrado = 0
i= int(input('Insira o número de bandejas:'))
for i in range(i):
    lata,copo = input('Insira o número de latas e copos:').split()
    lata = int(lata)
    copo = int(copo)
    if lata > copo:
        copoquebrado += copo
    else:
        continue
print(copoquebrado)'''

#14

#15

#16
'''resp = 'S'
while resp == 'S':
    jogador1 = input('Digite a sua jogada:').upper()
    jogador2 = input('Digite a jogada do outro jogador:').upper()
    if jogador1 == 'PEDRA' and jogador2 == 'PEDRA':
        print('Empate.')
    elif jogador1 == 'PEDRA' and jogador2 == 'TESOURA':
        print('Vitória!')
    elif jogador1 == 'PEDRA' and jogador2 == 'PAPEL':
        print('Derrota...')
    elif jogador1 == 'PAPEL' and jogador2 == 'PEDRA':
        print('Vitória!')
    elif jogador1 == 'PAPEL' and jogador2 == 'TESOURA':
        print('Derrota...')
    elif jogador1 == 'PAPEL' and jogador2 == 'PAPEL':
        print('Empate.')
    elif jogador1 == 'TESOURA' and jogador2 == 'PEDRA':
        print('Derrota...')
    elif jogador1 == 'TESOURA' and jogador2 == 'TESOURA':
        print('Empate.')
    elif jogador1 == 'TESOURA' and jogador2 == 'PAPEL':
        print('Vitória!')
    resp = input('Deseja continuar?').upper()
print('Fim')
'''
    
#17
'''x, y ,z = input("Insira três números inteiros:").split()
x = int(x)
y = int(y)
z = int(z)

if x < y < z:
    print(x,y,z)
elif x < z < y:
    print(x,z,y)
elif y < x < z:
    print(y,x,z)
elif y < z < x:
    print(y,z,x)
elif z < x < y:
    print(z,x,y)
elif z < y < x:
    print(z,y,x)'''
