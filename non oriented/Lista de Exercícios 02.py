#Lista de Exercícios 02

#01
'''valor = int(input("Qual o valor da casa?:"))
salario = int(input("Qual o seu salario?:"))
tempo = int(input("Em quanto anos você vai pagar?:"))
prestacao = valor/(tempo*12)

if(prestacao > salario*0.3):
    print("Empréstimo negado.")
else:
    print("Empréstimo concedido!")'''
    
#02
'''valor = float(input("Qual é o valor do produto?:"))
print("a. à vista(dinheiro ou cheque) – 10% de desconto")
print("b. 1x no cartão                – 5% de desconto")
print("c. 2x cartão                   – preço normal")
print("d. 3x ou mais no cartão        – 20% de juros")
opcao = input("Qual a opção de pagamento?:")

if opcao == 'a':
    print(valor*0.9)
else:
    if opcao == 'b':
        print(valor*0.95)
    else:
        if opcao == 'c':
            print(valor)
        else:
            if opcao == 'd':
                print(valor*1.2)
            else:
                print("Opção invalida.")'''

#02 elif
'''valor = float(input("Qual é o valor do produto?:"))
print("a. à vista(dinheiro ou cheque) – 10% de desconto")
print("b. 1x no cartão                – 5% de desconto")
print("c. 2x cartão                   – preço normal")
print("d. 3x ou mais no cartão        – 20% de juros")
opcao = input("Qual a opção de pagamento?:")

if opcao == 'a':
    print(valor*0.9)
elif opcao == 'b':
    print(valor*0.95)
elif opcao == 'c':
    print(valor)
elif opcao == 'd':
    print(valor*1.2)
else:
    print("Opção invalida.")'''

#03
'''peso = float(input("Insira seu peso:"))
altura = float(input("Insira sua altura:"))
imc = peso/(altura*altura)

if imc < 18.5 :
    print("Seu IMC é abaixo do peso.")
elif imc < 25 :
    print("Seu IMC é peso ideal.")
elif imc < 30 :
    print("Seu IMC é sobrepeso.")
elif imc < 40 :
    print("Seu IMC é obesidade.")
else:
    print("Seu IMC é obesidade mórbida.")'''
    
#04
'''n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))
n3 = float(input("Digite sua terceira nota:"))
media = (n1 + n2 +n3)/3

if media < 5:
    print("Reprovado.")
elif media < 7:
    print("Em recuperação.")
else:
    print("Aprovado!")'''

#05 
'''sal = float(input("Digite o valor do seu salário:"))

if sal <= 2000 :
    print("Isento")
elif sal <= 3000 :
    salate3000 = (sal - 2000) * 0.08
    print("R$ {:.2f}".format(salate3000))
elif sal <= 4500 :
    salate4500 = 80 + ((sal - 3000) * 0.18)
    print("R$ {:.2f}".format(salate4500))
else:
    salacima4500 = 80 + 270 + ((sal - 4500) * 0.28)
    print("R$ {:.2f}".format(salacima4500))'''
    

#06 não fazer

#07
'''ddd = int(input("Digite um DDD:"))
if ddd == 61 :
    print("Brasilia")
elif ddd == 71 :
    print("Salvador")
elif ddd == 11 :
    print("Sao Paulo")
elif ddd == 21 :
    print("Rio de Janeiro")
elif ddd == 32 :
    print("Juiz de Fora")
elif ddd == 19 :
    print("Campinas")
elif ddd == 27 :
    print("Vitoria")
elif ddd == 31 :
    print("Belo Horizonte")
else :
    print("DDD não cadastrado")'''

#08

'''num = int(input("Digite um número inteiro:"))

if num == 1 :
    print("January")
elif num == 2 :
    print("February")
elif num == 3 :
    print("March")
elif num == 4 :
    print("April")
elif num == 5 :
    print("May")
elif num == 6 :
    print("June")
elif num == 7 :
    print("July")
elif num == 8 :
    print("August")
elif num == 9 :
    print("September")
elif num == 10 :
    print("October")
elif num == 11:
    print("November")
else:
    print("December")'''

#09
'''a , b , c = input("Digite os valores de A, B e C:").split()
a = float(a)
b = float(b)
c = float(c)
delta = b**2 - (4 * a * c)
bhaskara1 = (-b + (delta ** 0.5))/ (2 * a)
bhaskara2 = (-b - (delta ** 0.5))/ (2 * a)

if a == 0 or delta < 0 :
    print("Impossivel calcular")
else:
    print("{:.5f}".format(bhaskara1))
    print("{:.5f}".format(bhaskara2))'''
    
#10
'''a, b , c = input("Digite a pontuação dos 3 competidores:").split()
a = int(a)
b = int(b)
c = int(c)

if a < 1 or a > 100 or b < 1 or b > 100 or c < 1 or c > 100 :
    print("Valores entre 1 e 100.")
elif a > b > c :
    print(b)
elif a > c > b :
    print(c)
elif b > a > c :
    print(a)
elif b > c > a :
    print(c)
elif c > b > a :
    print(b)
elif c > a > b :
    print(a)
else :
    print("Se vira não sei o que deu")'''

#11
'''cv , ce , cs , fv , fe , fs = input("Insira as Vitórias ,Empates e Saldo de Gols do Cormengo e Flaminthians:").split()
cv = int(cv)
ce = int(ce)
cs = int(cs)
fv = int(fv)
fe = int(fe)
fs = int(fs)

pontc = ((3 * cv) + ce)
pontf = ((3 * fv) + fe)

#Tentativa
#if 0 > cv == ce == fv == fe > 100 or -1000 > cs == fs > 1000 :
#    print("Valores inválidos.")
  
if cv < 0 or cv > 100 or ce < 0 or ce > 100 or fv < 0 or fv > 100 or fe < 0 or fe > 100 or cs < -1000 or cs > 1000 or fs < -1000 or cs > 1000 :
    print('Valores inválidos.')

else :
    if pontc > pontf :
        print('C')
    elif pontf > pontc :
        print('F')
    else:
        if cs > fs :
            print('C')
        elif fs > cs :
            print('F')
        else :
            print('=')'''

#12 ?

#13 mais de 1 teste
'''n = int(input("Digite o número de testes:"))
v1 = int(input("Digite o valor da primeira fileira:"))
v2, v3 , v4 , v5 = input("Digite os valores da segunda fileira:").split()
v2 = int(v2)
v3 = int(v3)
v4 = int(v4)
v5 = int(v5)
v6 = int(input("Digite o valor da terceira fileira:"))
soma1 = v1 + v6
soma2 = v2 + v4
soma3 = v3 + v5

dadoverdadeiro = soma1 + soma2 + soma3

if dadoverdadeiro == 21 :
    print("SIM")
else :
    print("NAO")'''

#14

'''inicio, fim = input("Digite a hora inicial e final do jogo:").split()
inicio = int(inicio)
fim = int(fim)

if fim > inicio :
    tempofi = fim - inicio
    print("O JOGO DUROU",tempofi,"HORA(S)")
    
elif fim == inicio:
    print("O JOGO DUROU 24 HORA(S)")
#inicio > fim    
else :
    tempoif = (24 - inicio) + fim
    print("O JOGO DUROU",tempoif,"HORA(S)")'''

#15

'''hi , mi , hf , mf = input("Insira hora inicial, minuto inicial, hora final e minuto final de um jogo:").split()
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

horasfi = hf - hi
minfi = mf - mi
horasif = (24 - hi) + hf
minif = (60 - mi) + mf

if (hf - hi) == 1 and mi > mf :
    print("O JOGO DUROU 0 HORA(S) E",minif,"MINUTO(S)")   
else:
    if hf > hi and mf > mi :
        print("O JOGO DUROU",horasfi,"HORA(S) E",minfi,"MINUTO(S)")
    elif hf > hi and mf < mi :
        print("O JOGO DUROU",horasfi,"HORA(S) E",minif,"MINUTO(S)")
    elif hf > hi and mf == mi :
        print("O JOGO DUROU",horasfi,"HORA(S) E 0 MINUTO(S)")
    elif hf < hi and mf > mi :
        print("O JOGO DUROU",horasif,"HORA(S) E",minfi,"MINUTO(S)")
    elif hf < hi and mf < mi :
        print("O JOGO DUROU",horasif,"HORA(S) E",minif,"MINUTO(S)")
    elif hf < hi and mf == mi :
       print("O JOGO DUROU",horasif,"HORA(S) E 0 MINUTO(S)")
    elif hf == hi and mf == mi :
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    elif hf == hi and mf > mi :
        print("O JOGO TEM DURAÇÃO MAXIMA DE 24 HORAS")
    else :
        min = (mi - mf)
        print("O JOGO DUROU 23 HORAS(S) e",min,"MINUTO(S)")'''

#16
'''diam = int(input("Insira o diâmetro da bola de boliche:"))
raio = diam/2
volesf = (4/3) * (3.14 * raio ** 3)
alt , larg , prof = input("Insira a altura, largura e profundidade da caixa:").split()
alt = int(alt)
larg = int(larg)
prof = int(prof)
vol = alt * larg * prof

if vol >= volesf :
    print("S")
else:
    print("N")'''

#17
'''sal = float(input("Insira seu salário:"))
if sal < 0 :
    print("Salário invalido.")
elif sal <= 400 :
    sal15 = sal * 1.15
    print("Novo salário: {:.2f}".format(sal15))
    print("Reajuste ganho: {:.2f}".format(sal15 - sal))
    print("Em percentual: 15 %")
elif sal <= 800 :
    sal12 = sal * 1.12
    print("Novo salário: {:.2f}".format(sal12))
    print("Reajuste ganho: {:.2f}".format(sal12 - sal))
    print("Em percentual: 12 %")
elif sal <= 1200 :
    sal10 = sal * 1.1
    print("Novo salário: {:.2f}".format(sal10))
    print("Reajuste ganho: {:.2f}".format(sal10 - sal))
    print("Em percentual: 10 %")
elif sal <= 2000 :
    sal7 = sal * 1.07
    print("Novo salário: {:.2f}".format(sal7))
    print("Reajuste ganho: {:.2f}".format(sal7 - sal))
    print("Em percentual: 7 %")
else :
    sal4 = sal * 1.04
    print("Novo salário: {:.2f}".format(sal4))
    print("Reajuste ganho: {:.2f}".format(sal4 - sal))
    print("Em percentual: 4 %")'''

#18

'''altc , largc , compc = input("Insira a altura ,largura e comprimento do colchão:").split()
altc = int(altc)
largc = int(largc)
compc = int(compc)
altp, largp = input("Insira a altura e a largura da porta:").split()
altp = int(altp)
largp = int(largp)

if altc > largp :
    print("N")
elif altc < largp and largc <= altp or compc <= altp :
    print("S")
else:
    print("N")'''
    
#19
'''a , b , c , d = input("Insira quatro valores inteiros:").split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and (a%2) == 0 :
    print("Valores aceitos")
else :
    print("Valores nao aceitos")'''

#20
'''codigo , quantidade = input("Digite o código do produto e a quantidade:").split()
codigo = int(codigo)
quantidade = int(quantidade)
if codigo == 1 :
    print("Total: R${:.2f}".format(4 * quantidade))
elif codigo == 2 :
    print("Total: R${:.2f}".format(4.5 * quantidade))
elif codigo == 3 :
    print("Total: R${:.2f}".format(5 * quantidade))
elif codigo == 4 :
    print("Total: R${:.2f}".format(2 * quantidade))
elif codigo == 5 :
    print("Total: R${:.2f}".format(1.5 * quantidade))
else:
    print("Código inválido.")'''

#21
competidores , folhas , cada = input("Insira o número de competidores, a quantidade folhas compradas e quanto cada competidor deve receber:").split()
competidores = int(competidores)
folhas = int(folhas)
cada = int(cada)
folhasnecess = competidores * cada
if folhasnecess > folhas :
    print("N")
else :
    print("S")

#22 ?
