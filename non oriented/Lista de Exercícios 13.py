#Lista de Exercícios 13
#01
'''n = int(input('Indique a quantidade de idas à feira:'))
produtos = []
info = {}

for i in range(n):
    m = int(input('Digite a quantidade de produtos disponíveis:'))
    for j in range(m):
        produto = input('Digite o nome do produto e seu preço:').split()
        produto[1] = float(produto[1])
        info = {'nome':produto[0],'preço':produto[1]}
        produtos.append(info)
    print(produtos)
    p = int(input('Digite a quantidade de produtos comprados:'))
    valor = 0
    for k in range(p):
        item,quant = input('Insira o item e a quantidade:').split()
        quant = int(quant)
        for x in range(len(produtos)):
            if produtos[x]['nome'] == item :
                valor += (produtos[x]['preço']) * quant
    print('R${:.2f}'.format(valor))'''
    
#02
'''trad = {}
t = int(input('Insira a quantidade de traduções:'))
for i in range(t):
    trad[input('Digite a língua:')]= input('Digite a tradução:')
m = int(input('Insira a quantidade de crianças que receberão cartas:'))
for i in range(m):
    nome = input('Digite o nome da criança:')
    lingua = input('Insira a língua nativa da criança:').lower()
    print(nome)
    print(trad.get(lingua))
    print()'''

    
#04
'''natal = {}
natal['brasil']  =            'Feliz Natal!'
natal['alemanha']  =          'Frohliche Weihnachten!'
natal['austria']   =          'Frohe Weihnacht!'
natal['coreia']    =          'Chuk Sung Tan!'
natal['espanha']   =          'Feliz Navidad!'
natal['grecia']     =         'Kala Christougena!'
natal['estados-unidos'] =     'Merry Christmas!'
natal['inglaterra']   =       'Merry Christmas!'
natal['australia']    =       'Merry Christmas!'
natal['portugal']   =         'Feliz Natal!'
natal['suecia']     =         'God Jul!'
natal['turquia']    =         'Mutlu Noeller'
natal['argentina']    =       'Feliz Navidad!'
natal['chile']      =         'Feliz Navidad!'
natal['mexico']      =        'Feliz Navidad!'
natal['antardida']    =       'Merry Christmas!'
natal['canada']       =       'Merry Christmas!'
natal['irlanda']      =       'Nollaig Shona Dhuit!'
natal['belgica']      =       'Zalig Kerstfeest!'
natal['italia']        =      'Buon Natale!'
natal['libia']        =      'Buon Natale!'
natal['siria']        =       'Milad Mubarak!'
natal['marrocos']     =       'Milad Mubarak!'
natal['japao']         =      'Merii Kurisumasu!   '

país = input('Digite o país para saber como falar Feliz Natal no idioma local:').lower()
print(natal.get(país,'--- NOT FOUND ---'))'''


#05
'''while True:
    n = int(input('Insira a quantidade de numeros:'))
    if n == 0:
        break
    lista = [int(x) for x in input('Insira os números:').split()]
    lista.sort()
    for i in range(len(lista)):
        if i%2 == 0: #par
            if i+1 == (len(lista)):
                print(lista[i])
                break
            elif lista[i] == lista[i+1]:
                continue
            else:
                print(lista[i])
                break
        else:
            continue'''

#08
lista = {}
n = int(input('Insira a quantidade de pessoas:'))
for i in range(n):
    lista[input('Digite o nome da pessoa:')] = input('Digite os três presentes:').split()
print(lista)
while True:
    nome,presente = input('Digite o nome do seu amigo e o presente:').split()
    for i in lista:
        aux = 0
        if i == nome:
            for x in lista[i]:
                if x == presente:
                    print('Uhul! Seu amigo secreto vai adorar o/')
                    aux += 1
                    break
        else:
            continue
        if aux == 0:
            print('Tente Novamente!')
        else:
            continue
    
    