#Simulado 01
#Questao 01

'''instancias = int(input('Indique o numero de instâncias:'))
for i in range(instancias):
    cons,dig = [int(x) for x in input('Indique a quantidade de consoantes e dígitos:').split()]
    if cons == 0 and dig == 0:
        print('0')
    else:
        calculocons = 26 ** cons
        calculodig = 10 ** dig
        print(calculocons * calculodig)'''



#Questao 02

n = int(input('Insira o número de pessoas que o sensor detectou:'))
while n < 0 or n > 10:
    n = int(input('Insira um valor válido:'))
contador = 0
tempoligado = 0
ultimoinstante = 0
while n > contador:
    instante = int(input('Insira o instante em que a pessoa passou:'))
    while instante < 0 or instante > 100:
        instante = int(input('Insira um valor válido:'))
    contador += 1
    tempoligado += 10
    if contador > 1 :
        difinstante = instante - ultimoinstante
        if difinstante < 10:
            tempoligado = tempoligado - (10 - difinstante)
            ultimoinstante = instante
        else:
            ultimoinstante = instante
    else:
        ultimoinstante = instante
print(tempoligado)

#Questao 03
'''def soma(inicio,fim):
    somai = 0
    for i in range(inicio,fim+1):
       somai += i
    print(somai)
       
def subtracao(a,b):
    if a > b:
        print(a - b)
    else:
        print(b - a)
    

while True:
    inicio,fim = [int(x) for x in input('Insira o intervalo:').split()]
    while inicio > fim:
        inicio,fim = [int(x) for x in input('Insira um intervalo válido:').split()]
    soma(inicio,fim)
    a,b = [int(x) for x in input('Digite 2 valores:').split()]
    subtracao(a,b)
    parada = input('Deseja continuar?').upper()
    if parada == 'N':
        break'''
    
#Questao 04

def encontraPrimos(n):
    primo = 0
    for i in range (2,intervalo):
        s1 = 0    
        for j in range(2,i):
            if (i%j == 0):
                s1 += 1
                break
        if s1 == 0:
            primo = i
            break
    return primo


verif = int(input('Número de verificações:'))
for x in range(verif):
    n, m =[int(x) for x in input('Digite os valores de N e M:').split()]
    while n < 2 or n > 100 or m < 2 or m > 100:
        n, m =[int(x) for x in input('Digite novamente:').split()]
    p1 = encontraPrimos(n)
    p2 = encontraPrimos(m)
    print(p1*p2)
print('Fim')



