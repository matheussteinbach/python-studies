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
    
    def locacao(self):
        lista = list()
        print("\nFILMES DISPONÍVEIS PARA LOCAÇÃO:")
        print("")
        for x in filmes:
            if x[2] == 'Livre':
                f = x[0]
                lista.append(f)
        return lista
    
    
class Funcionarios(Pessoa):
    def __init__(self,nome, cpf, idade,):
        super().__init__(nome, cpf, idade)
        
    def set_nome(self,nome):
        self.nome = nome
    
    def set_cpf(self,cpf):
        self.cpf = cpf
    
    def set_idade(self,idade):
        self.idade = idade
        

class Clientes(Pessoa):
    def __init__(self,nome, cpf, idade,fidelidade):
        super().__init__(nome, cpf, idade)
        self.fidelidade = fidelidade