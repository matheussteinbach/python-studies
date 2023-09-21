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
    
    def set_nome(self,nome):
        self.nome = nome
    
    def set_cpf(self,cpf):
        self.cpf = cpf
    
    def set_idade(self,idade):
        self.idade = idade
    
    def set_fidelidade(self,fidelidade):
        self.fidelidade = fidelidade
    
    def consultafilme(self):
        print('\nBANCA DE FILMES:')
        print()
        for x in filmes:
            print(f'{x[2]} - {x[0]} ({x[1]})')
    
    def consultadisponivel(self):
        lista = list()
        print("\nFILMES DISPONÍVEIS PARA LOCAÇÃO:")
        print("")
        for x in filmes:
            if x[2] == 'Livre':
                print(x[0])
            
    
    def locacao(self):
        self.consultadisponivel()
        filme = input('\nDigite o nome do filme: ')
        aux = 0
        while True:
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
                        print('Desculpa parte 2... Todos os filmes desse gênero estão alocados.')

            if aux == 0:
                filme = input('\nDigite um filme disponível: ')
            if aux == 1:
                break
            
        return calculo
    
    
class Funcionarios(Pessoa):
    def __init__(self,nome, cpf, idade,):
        super().__init__(nome, cpf, idade)
        
    def locacao(self):
        self.consultadisponivel()
        filme = input('\nDigite o nome do filme: ')
        aux = 0
        while True:
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
                        print('Desculpa parte 2... Todos os filmes desse gênero estão alocados.')

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

c4 = Clientes('Ismas','66',45,2)
listaclientes.append(c4)


filmes = [['Harry Potter','Ficção', 'Alocado'], ['Como Treinar seu Dragão','Ficção','Livre'],
          ['Star Wars','Ficção','Livre'], ['Se beber não case','Comédia','Livre'],
          ['Esposa de Mentirinha','Comédia','Livre'],['Pulp Fiction','Ação','Alocado'],
          ['Homem de Ferro','Ação','Livre'], ['Pânico','Terror','Alocado'],['Chucky','Terror','Livre'],
          ['Romeu e Julieta','Romance','Alocado'], ['A Culpa é das Estrelas','Romance','Livre']]


#main
faturamentoempresa = 0
while True:
    print()
    print('='*49)
    print('             BEM-VINDO À LOCADORA POO')
    print('FILMES APENAS 5 REAIS POR DIA (FORA OS DESCONTOS)')
    print('='*49)
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
                print('3 - CONSULTA FATURA')
                print('4 - CADASTRO FILME')
                print('5 - ALTERAR FILMES')
                print('6 - CADASTRO CLIENTE/FUNCIONÁRIOS')
                print('7 - ALTERAR/EXCLUIR CADASTRO')
                print('8 - CONSULTA FATURAMENTO DA EMPRESA')
                print('9 - CONSULTA BANCO DE CLIENTES')
                print('\n0 - SAIR')
                opcao = int(input("\nDigite a opção escolhida: "))
                while not(0<=opcao<=9):
                    opcao = int(input("Opção inválida. Digite novamente: "))
            
                if opcao == 1:
                    calculo = func.locacao()
                    fatura += calculo
                    faturamentoempresa += calculo
                    
                elif opcao == 2:
                    func.consultafilme()
                        
                elif opcao == 3:
                    print('\nSua fatura está no valor de: R$',fatura)
                    
                elif opcao == 4:
                    print('\nCADASTRANDO FILME...')
                    nome = input('Insira o nome do filme a ser cadastrado: ')
                    genero = input('Insira o gênero: ')
                    filme = [nome,genero,'Livre']
                    filmes.append(filme)
                
                elif opcao == 5:
                    aux5 = 0
                    print('\nALTERANDO INFORMAÇÕES...')
                    nomefilme = input('Digite o atual nome do filme que deseja alterar:')
                    for x in filmes:
                        if x[0] == nomefilme:
                            x[0] = input('Digite o novo nome do filme: ')
                            x[1] = input('Digite o novo gênero: ')
                            x[2] = input('Digite o novo status: ')
                            print('Filme alterado com sucesso.')
                            aux5 = 1
                            
                    if aux5 == 0:
                        print('Filme não encontrado na nossa banca...')
                    
                
                elif opcao == 6:
                    print('\nCADASTRANDO...')
                    resp = int(input('Digite 1 para cadastrar funcionário ou 2 para cliente: '))
                    while resp != 1 and resp != 2:
                        resp = int(input('Digite 1 para cadastrar funcionário ou 2 para cliente: '))
            
                    if resp == 1:
                        nome = input("\nDigite o nome do funcionário: ")
                        cpff = input('Digite o CPF: ')
                        idade = int(input("Digite a idade: "))
                        f = Funcionarios(nome,cpff,idade)
                        listafuncionarios.append(f)
            
                    elif resp == 2:
                        nome = input("\nDigite o nome do cliente: ")
                        cpfc = input('Digite o CPF: ')
                        idade = int(input("Digite a idade: "))
                        c = Clientes(nome,cpfc,idade,0)
                        listaclientes.append(c)
                        
                elif opcao == 7:
                    aux3 = 0
                    while True:
                        resp = input('\nDigite o atual CPF da pessoa que deseja alterar/excluir o cadastro: ')
                        resp2 = int(input('Digite 1 se deseja alterar e 2 para excluir: '))
                        while resp2 != 1 and resp2 != 2:
                            resp2 = int(input('Digite 1 se deseja alterar e 2 para excluir: '))
                        if resp2 == 1:
                            for func in listafuncionarios:
                                if resp == func.get_cpf():
                                    aux3 = 1
                                    novonome = input('Digite o novo nome: ')
                                    novocpf = input('Digite o novo CPF: ')
                                    novaidade = int(input('Digite a nova idade: '))
                                    func.set_nome(novonome)
                                    func.set_cpf(novocpf)
                                    func.set_idade(novaidade)
                                    if resp == cpf and novocpf != cpf:
                                        cpf = novocpf
                            
                            for cliente in listaclientes:
                                if resp == cliente.get_cpf():
                                    aux3 = 1
                                    novonome = input('Digite o novo nome: ')
                                    novocpf = input('Digite o novo CPF: ')
                                    novaidade = int(input('Digite a nova idade: '))
                                    novafidelidade = int(input('Digite a nova fidelidade: '))
                                    cliente.set_nome(novonome)
                                    cliente.set_cpf(novocpf)
                                    cliente.set_idade(novaidade)
                                    cliente.set_fidelidade(novafidelidade)
                                
                        elif resp2 == 2:
                            if resp == cpf:
                                print('Não é possivel excluir o próprio cadastro.')
                                break
                            for i, j in enumerate(listafuncionarios): 
                                if resp == j.get_cpf():
                                    aux3 = 1
                                    listafuncionarios.pop(i)
                                    print('Funcionário excluido com sucesso.')
                                    
                            for i, j in enumerate(listaclientes): 
                                if resp == j.get_cpf():
                                    aux3 = 1
                                    listaclientes.pop(i)
                                    print('Cliente excluido com sucesso.')
                            
                        
                        if aux3 == 0:
                            print('CPF INVÁLIDO.')
                        
                        if aux3 == 1:
                            break
                        
                
                elif opcao == 8:
                    print('O faturamento da empresa Locadora POO está no valor de: R$',faturamentoempresa,', hoje!')
        
                elif opcao == 9:
                    print('\nFUNCIONÁRIOS:')
                    for y in listafuncionarios:
                        print(f'NOME: {y.get_nome()} - CPF: {y.get_cpf()} - IDADE: {y.get_idade()}')
                    print('\nCLIENTES:')
                    for x in listaclientes:
                        print(f'NOME: {x.get_nome()} - CPF: {x.get_cpf()} - IDADE: {x.get_idade()} - FIDELIDADE: {x.get_fidelidade()}')
        
                elif opcao == 0:
                    print('\nSua fatura ficou no valor de: R$',fatura)
                    print('SAINDO...')
                    sair = 1
           
        if sair == 1:
            break
            
        for cliente in listaclientes:
            if cpf == cliente.get_cpf():
                aux = 1
                print('\nMENU:')
                print('1 - LOCAÇÃO DE FILME')
                print('2 - CONSULTA FILMES')
                print('3 - CONSULTA FATURA')
                print('\n4 - SAIR')
                opcao = int(input("\nDigite a opção escolhida: "))
                while not(1<=opcao<=5):
                    opcao = int(input("Opção inválida. Digite novamente: "))
                    
                if opcao == 1:
                    calculo = cliente.locacao()
                    fatura += calculo
                    faturamentoempresa += calculo
                    
                elif opcao == 2:
                    cliente.consultafilme()
                    
                elif opcao == 3:
                    print('\nSua fatura está no valor de: R$',fatura)
                    
                elif opcao == 4:
                    print('\nSua fatura ficou no valor de: R$',fatura)
                    print('SAINDO...')
                    print()
                    sair = 1
        
        if sair == 1:
            break

        if aux == 0:
            print('\nCPF NÃO CADASTRADO.')
            op = int(input('Digite 1 para digitar novamente o CPF e 2 para cadastrar: '))
            while op != 1 and op != 2:
                op = int(input('Digite 1 para digitar novamente o CPF e 2 para cadastrar: '))
            if op == 1:
                break
            elif op == 2:
                print("\nCLIENTE AINDA NÃO CADASTRADO... INICIANDO CADASTRO:")
                nome = input("\nDigite o seu nome: ")
                idade = int(input("Digite a sua idade: "))
                c = Clientes(nome,cpf,idade,0)
                listaclientes.append(c)