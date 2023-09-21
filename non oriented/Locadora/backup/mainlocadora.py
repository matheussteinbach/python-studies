class Pessoa:
    def __init__(self,nome,cpf,idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        
    def get_nome(self):
        return self.nome
    
    def get_cpf(self):
        return self.cpf
    
    def get_idade(self):
        return self.idade
    
    def get_fidelidade(self):
        return self.fidelidade
    
    def set_fidelidade(self,fidelidade):
        self.fidelidade = fidelidade
    
    
    def consultafilme(self):
        lista = list()
        print("\nFILMES DISPONÍVEIS PARA LOCAÇÃO:")
        print("")
        for x in filmes:
            if x[2] == 'Livre':
                print(x[0])
            
    
    def locacao(self):
        self.consultafilme()
        filme = input('\nDigite o nome do filme: ')
        aux = 0
        while True:
            aux3 = 0
            aux2 = 0
            for y in filmes:
                if y[0] == filme and y[2] == 'Livre':
                    dias = int(input(f'Por quantos dias você deseja alocar {filme}? '))
                    preco = 5 * dias
                    desconto = 0.1 * self.fidelidade
                    calculo = preco - desconto * preco
                    print(f'O seu filme foi alocado por {dias} dias com sucesso, no preço de: {calculo} reais')
                    y[2] = 'Alocado'
                    aux = 1
                    if self.fidelidade < 3:
                        self.set_fidelidade(self.fidelidade+1)
                        
                elif y[0] == filme and y[2] == 'Alocado':
                    print('Desculpe, seu filme ja está alocado... :(')
                    print('\nNossa indicação do mesmo gênero:')
                    for z in filmes:
                        if z[1] == y[1] and z[2] == 'Livre':
                            print(z[0])
                            aux2 = 1
                            
                        if aux2 == 0:
                            if aux3 == 0:
                                print('Desculpa parte 2... Todos os filmes desse gênero estão alocados.')
                                aux3 = 1

            if aux == 0:
                filme = input('\nDigite um filme disponível: ')
            if aux == 1:
                break
            
        return calculo
    
    
class Funcionarios(Pessoa):
    def __init__(self,nome, cpf, idade,):
        super().__init__(nome, cpf, idade)
        
    def set_nome(self,nome):
        self.nome = nome
    
    def set_cpf(self,cpf):
        self.cpf = cpf
    
    def set_idade(self,idade):
        self.idade = idade
        
    def locacao(self):
        self.consultafilme()
        filme = input('\nDigite o nome do filme: ')
        aux = 0
        while True:
            aux3 = 0
            aux2 = 0
            for y in filmes:
                if y[0] == filme and y[2] == 'Livre':
                    dias = int(input(f'Por quantos dias você deseja alocar {filme}? '))
                    while dias > 2:
                        dias = int(input(f'Limite de funcionários: 2 dias. Digite novamente: '))
                    preco = 5 * dias
                    desconto = 0.4
                    calculo = preco - desconto * preco
                    print(f'O seu filme foi alocado por {dias} dias com sucesso, no preço de: {calculo} reais')
                    y[2] = 'Alocado'
                    aux = 1
                    
                        
                elif y[0] == filme and y[2] == 'Alocado':
                    print('Desculpe, seu filme ja está alocado... :(')
                    print('\nNossa indicação do mesmo gênero:')
                    for z in filmes:
                        if z[1] == y[1] and z[2] == 'Livre':
                            print(z[0])
                            aux2 = 1
                            
                        if aux2 == 0:
                            if aux3 == 0:
                                print('Desculpa parte 2... Todos os filmes desse gênero estão alocados.')
                                aux3 = 1

            if aux == 0:
                filme = input('\nDigite um filme disponível: ')
            if aux == 1:
                break
            
        return calculo
        

class Clientes(Pessoa):
    def __init__(self,nome, cpf, idade,fidelidade):
        super().__init__(nome, cpf, idade)
        self.fidelidade = fidelidade
        

listafuncionarios = list()
listaclientes = list()

f1 = Funcionarios('Matheus','11',18)
listafuncionarios.append(f1)

f2 = Funcionarios('Thiago','22',18)
listafuncionarios.append(f2)

c1 = Clientes('Abacas','33',16,1)
listaclientes.append(c1)

c2 = Clientes('Jabas','44',19,3)
listaclientes.append(c2)

c3 = Clientes('Luciana','55',30,0)
listaclientes.append(c3)

filmes = [['Harry Potter','Ficção', 'Alocado',3], ['Como Treinar seu Dragão','Ficção','Livre',0],
          ['Se beber não case','Comédia','Livre',0],['Esposa de Mentirinha','Comédia','Livre',0],
          ['Pulp Fiction','Ação','Livre',0], ['Homem de Ferro','Ação','Livre',0],
          ['Pânico','Terror','Alocado',1],['Chucky','Terror','Livre',0]]


#main
faturamentoempresa = 0
while True:
    print('='*33)
    print('BEM-VINDO À LOCADORA POO')
    print('='*33)
    cpf = input('INSIRA SEU CPF PARA LOGIN: ')
    aux = 0
    fatura = 0
    
    while True:
        sair = 0
        for func in listafuncionarios:
            if cpf == func.get_cpf():
                aux = 1
                print('\nMENU:')
                print('1 - LOCAÇÃO DE FILME')
                print('2 - CONSULTA FILMES')
                print('3 - CONSULTA PRAZO DE ENTREGA')
                print('4 - CONSULTA FATURA')
                print('5 - CADASTRO CLIENTE/FUNCIONÁRIOS')
                print('6 - CONSULTA FATURAMENTO DA EMPRESA')
                print('7 - CONSULTA BANCO DE CLIENTES')
                print('\n8 - SAIR')
                opcao = int(input("\nDigite a opção escolhida: "))
                while not(1<=opcao<=8):
                    opcao = int(input("Opção inválida. Digite novamente: "))
            
                if opcao == 1:
                    calculo = func.locacao()
                    fatura += calculo
                    faturamentoempresa += calculo
                    
        
                elif opcao == 2:
                    for x in filmes:
                        print(f'{x[2]} - {x[0]} ({x[1]})')
                        
                elif opcao == 4:
                    print('\nSua fatura está no valor de:',fatura,'reais')
                
                elif opcao == 5:
                    resp = int(input('Digite 1 para cadastrar funcionário ou 2 para cliente: '))
                    while resp != 1 and resp != 2:
                        resp = int(input('Digite 1 para cadastrar funcionário ou 2 para cliente: '))
            
                    if resp == 1:
                        nome = input("\nDigite o nome do funcionário: ")
                        cpf = input('Digite o cpf:')
                        idade = int(input("Digite a idade: "))
                        f = Funcionarios(nome,cpf,idade)
                        listafuncionarios.append(f)
            
                    elif resp == 2:
                        nome = input("\nDigite o nome do cliente: ")
                        cpf = input('Digite o cpf:')
                        idade = int(input("Digite a idade: "))
                        c = Clientes(nome,cpf,idade,0)
                        listaclientes.append(c)
                        
                elif opcao == 6:
                    print('O faturamento da empresa Locadora POO está no valor de: R$',faturamentoempresa,',hoje')
        
                elif opcao == 7:
                    for x in listaclientes:
                        print(f'NOME: {x.get_nome()} - CPF: {x.get_cpf()} - IDADE: {x.get_idade()} - FIDELIDADE: {x.get_fidelidade()}')
        
                elif opcao == 8:
                    print('\nSua fatura ficou no valor de:',fatura,'reais')
                    print('SAINDO...')
                    print()
                    sair = 1
           
        if sair == 1:
            break
            
        for cliente in listaclientes:
            if cpf == cliente.get_cpf():
                aux = 1
                print('\nMENU:')
                print('1 - LOCAÇÃO DE FILME')
                print('2 - CONSULTA FILMES')
                print('3 - CONSULTA PRAZO DE ENTREGA')
                print('4 - CONSULTA FATURA')
                print('\n5 - SAIR')
                opcao = int(input("\nDigite a opção escolhida: "))
                while not(1<=opcao<=5):
                    opcao = int(input("Opção inválida. Digite novamente: "))
                    
                if opcao == 1:
                    calculo = cliente.locacao()
                    fatura += calculo
                    faturamentoempresa += calculo
                    
                elif opcao == 2:
                    for x in filmes:
                        print(f'{x[2]} - {x[0]} ({x[1]})')
                    
                elif opcao == 4:
                    print('\nSua fatura está no valor de:',fatura,'reais')
                    
                elif opcao == 5:
                    print('\nSua fatura ficou no valor de:',fatura,'reais')
                    print('SAINDO...')
                    print()
                    sair = 1
        
        if sair == 1:
            break

        if aux == 0:
             #print('CPF NÃO CADASTRADO.')
             #opcao = input('DESEJA DIGITAR NOVAMENTE OU CADASTRAR')
            print("\nCLIENTE AINDA NÃO CADASTRADO... INICIANDO CADASTRO: ")
            nome = input("\nDigite o seu nome: ")
            idade = int(input("Digite a sua idade: "))
            c = Clientes(nome,cpf,idade,0)
            listaclientes.append(c)
    