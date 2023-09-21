#Revisão Funções
#01
'''def verificacao(n):
    while (n != 0) and (n != 1):
        n = int(input('Valor inválido. Digite novamente:'))
    return n

while True:
    a = verificacao(int(input('Insira os valor escolhido por Alice:')))
    b = int(input('Insira os valor escolhido por Beto:'))
    b = verificacao(b)
    c = verificacao(int(input('Insira os valor escolhido por Clara:')))
    
    if a == 0 and b == 0 and c == 0:
        print('Fim do programa.')
        break
    elif a == 1 and b == 1 and c == 1:
        print('*')
    elif a == 1 and b == 0 and c == 0:
        print('A')
    elif a == 0 and b == 1 and c == 1:
        print('A')
    elif a == 1 and b == 0 and c == 1:
        print('B')
    elif a == 0 and b == 1 and c == 0:
        print('B')
    elif a == 0 and b == 0 and c == 1:
        print('C')
    elif a == 1 and b == 1 and c == 0:
        print('C')'''

#02
'''def entrada(n):
    while n < 1 or n > 100:
        n = int(input('Insira um valor válido:'))
    return n

def calcula_distancia(t,v):
    dist = v*t
    return dist

soma = 0
n = int(input('Insira a quantidade de intervalos:'))
while n < 1 or n > 10:
    n = int(input('Insira um valor válido:'))
for i in range(n):
    t,v = [int(x) for x in input('Insira o tempo decorrido e a velocidade média:').split()]
    t = entrada(t)
    v = entrada(v)
    dist = calcula_distancia(t,v)
    soma += dist
print('Distância total percorrida:',soma,'considerando os',n,'trechos')'''

#03
def verificacao(n):
    while n < 0 or n > 100:
        n = int(input('Insira um valor válido:'))
    return n

def calculo(x,y):
    area = (x*y)/2
    perimetro = ((((x/2)**2) + ((y/2)**2))**0.5)*4
    return area,perimetro

n = int(input('Insira o número de pipas que serão construídas:'))
for n in range(n):
    x,y = [int(x) for x in input('Digite x e y:').split()]
    x = verificacao(x)
    y = verificacao(y)
    area,perimetro = calculo(x,y)
    print('Área:',int(area),'cm2      Perímetro:',int(perimetro),'cm')

#04
def verificacao(n):
    while n < 2 or n > 300:
        n = int(input('Digite um valor válido:'))
    return n

def descobreprimo(n):
    contador = 0
    primo = 0
    for i in range(2,n):
        if n%i == 0:
            contador += 1
    if contador == 0:
        primo += 1
        print('É primo!')
        return primo
        
contaprimo = 0     
for i in range(10):
    n = verificacao(int(input('Digite um número inteiro:')))
    primo = descobreprimo(n)
    if primo == 1:
        contaprimo += 1

print('Contador de primos:',contaprimo)










    