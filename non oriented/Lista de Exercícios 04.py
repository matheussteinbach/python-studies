#Lista de Exercícios 04

#01
'''sexo = input("Insira seu sexo:").upper()

while  sexo != 'M' and sexo != 'F':
    sexo = input("Só aceitamos M ou F:").upper()
print('Seu sexo é:',sexo)'''

#02

'''from random import randrange
num = randrange(11)
cont = 1
teclado = int(input('Tente acertar o número!:'))
while teclado != num:
    teclado = int(input('Digite outro valor:'))
    cont += 1
print('Parabéns, você acertou em',cont,'tentativas!')'''

#03 
salario = int(input('Digite o salário do funcionario:'))
descontoprev = salario * 0.11
if descontoprev > 320:
    descontoprev = 320
    x = 320/salario
    print("O percentual de desconto previdenciario foi de:",x*100,"%.")
else:
    print("O valor do desconto previdenciario é:",descontoprev)

#04
'''num = int(input('Digite um valor inteiro:'))
for i in range(1, 10001):
    if i%num == 2:
        print(i)
    else:
        continue'''
#05
'''num = int(input('Digite um valor inteiro para saber a tabuada!:'))
for i in range(11):
    print(i,'x', num,'=',i*num)'''

#06
'''x = 1
num = int(input('Digite um número inteiro:'))
if num == 0:
    print('')
else:
    while x <= num:
        print(x, end=' ')
        x += 1
        if x > num:
            break'''

#07
'''somaa= 0
somag= 0
somad= 0
codigo = int(input("Insira o código do produto:"))

while codigo != 4:
    if codigo == 1:
        somaa += 1
        codigo = int(input("Insira o código do produto:"))
    elif codigo == 2:
        somag += 1
        codigo = int(input("Insira o código do produto:"))
    elif codigo == 3:
        somad += 1
        codigo = int(input("Insira o código do produto:"))
    else:
        codigo = int(input("Insira um valor válido:"))
    
print("MUITO OBRIGADO")
print("Alcool:",somaa)
print("Gasolina:",somag)
print("Diesel:",somad)'''
    

#08
'''m,n = input("Insira um par de valores inteiros:").split()
m = int(m)
n = int(n)
soma = 0
if m <= 0 or n <= 0:
    print("")
elif n > m:
    for i in range (m,n+1):
        soma += i
        print(i, end=' ')
    print("Sum =",soma)
elif m > n:
    for i in range (n,m+1):
        soma += i
        print(i, end=' ')
    print("Sum =",soma)'''
    
    







