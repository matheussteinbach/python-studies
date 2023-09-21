#Lista de Exercícios 01

#1003
'''n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
soma = n1 + n2
print("Soma:",soma)'''

#1004
'''n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
prod = n1 * n2
print("Produto:",prod)'''

#1005
'''notaA = float(input("Digite a sua nota:"))
notaB = float(input("Digite a sua outra nota:"))
media = (notaA*3.5 + notaB*7.5)/11
print("Média:{:.5f}".format(media))'''

#1006
'''notaA = float(input("Digite sua primeira nota:"))
notaB = float(input("Digite sua segunda nota:"))
notaC = float(input("Digite sua terceira nota:"))
media = (notaA*2 + notaB*3 + notaC*5)/10
print("Média:{:.1f}" .format(media))'''

#1007
'''nA = int(input("Digite um número:"))
nB = int(input("Digite outro número:"))
nC = int(input("Digite mais um número:"))
nD = int(input("É o último número eu juro:"))
DIFERENÇA = nA * nB - nC * nD
print("A Diferença dos produtos é:",DIFERENÇA)'''

#1008
'''numF = (input("Digite seu número de funcionário:"))
ht = int(input("Por quantas horas você trabalhou esse mês?:"))
vh = float(input("Quanto você recebe por hora?:"))
salario = ht * vh
print("NÚMERO:",numF)
print("SALÁRIO: R${:.2f}".format(salario))'''

#1008 outra forma
'''numF = (input("Digite seu número de funcionário:"))
ht = int(input("Por quantas horas você trabalhou esse mês?:"))
vh = float(input("Quanto você recebe por hora?:"))
salario = ht * vh
print("O funcionário de número",numF,"recebeu: R${:.2f}".format(salario),"esse mês.")'''

#2374 dúvida em como fazer 1 ≤ N ≤ 40 e 1 ≤ M ≤ 40
'''n = int(input("Pressão desejada:"))
m = int(input("Pressão lida pela bomba:"))
dif = n - m
print(dif)'''

#2431 ?

#1012 dúvida formatação da variável

'''a = float(input("Digite o valor de A:")) 
b = float(input("Digite o valor de B:")) 
c = float(input("Digite o valor de C:"))
pi = 3.14159
triangulo = (a * c)/2
circulo = pi * c ** 2
trapezio = ((a + b) * c)/2
quadrado = b * b
retangulo = a * b

print("{:.3f}".format(triangulo))
print("{:.3f}".format(circulo))
print("{:.3f}".format(trapezio))
print("{:.3f}".format(quadrado))
print("{:.3f}".format(retangulo))'''

#1020

'''idadedias = int(input("Informe sua idade em dias:"))
anos = idadedias/365
meses = (idadedias%365)/30
dias = (idadedias%365)%30
print (int(anos),"ano(s)")
print (int(meses),"mes(es)")
print (int(dias),"dia(s)")'''


#1015

x1, y1 = input("Digite as coordenadas x1 e y1 separados por um espaço:").split()
x1 = float(x1)
y1 = float(y1)

x2, y2 = input("Digite as coordenadas x2 e y2 separadas por um espaço:").split()
x2 = float(x2)
y2 = float(y2)

dist = (((( x2 - x1 ) ** 2) + ((y2 - y1) ** 2)) ** 0.5)
print ("{:.4f}".format(dist))

#1019

'''durseg = int(input("Informe o tempo do evento em segundos:"))

horas = durseg/3600
minutos = (durseg%3600)/60
segundos = (durseg%3600)%60


print(int(horas),";",int(minutos),";",int(segundos))'''

#1017

'''t = int(input("Tempo gasto na viagem(em horas):"))
vm = int(input("Velocidade média(em km/h):"))
#consumo 12 KM/L
gasto = (vm * t)/12
print("O gasto foi de:{:.3f}".format(gasto),"litros")'''

#1014

'''x = float(input("Distância total percorrida (em Km):"))
y = float(input("Total de combustivel gasto (em litros):"))
consmed = x / y
print("O consumo médio é de:{:.3f}".format(consmed),"Km/L")'''

#1009

'''nome = input("Nome do vendedor:")
salfix = float(input("Valor do salário fixo:"))
totven = float(input("Quanto foi o seu total de vendas efetudas(em dinheiro):"))

sbonus = salfix + totven * 0.15

print("TOTAL = RS$ {:.2f}".format(sbonus))'''


