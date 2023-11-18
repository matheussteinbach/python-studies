import pickle


'''clientes = {}
clientes[123] = 'Davi'
clientes[456] = 'da silva'
print(clientes)
arq_clientes = open('clientes.pkl', 'wb')
pickle.dump(clientes, arq_clientes)'''

def leitura():
    arq_clientes = open('clientes.pkl', 'rb')
    clientes = pickle.load(arq_clientes)
    print(clientes)
    arq_clientes.close()
    return clientes

def escrita():
    arq_clientes = open('clientes.pkl', 'wb')
    pickle.dump(clientes, arq_clientes)
    arq_clientes.close()

while True:
    clientes = leitura()
    cpf = input('Entre com o CPF: ')
    nome = input('Entre com o Nome: ')
    clientes[cpf] = nome
    escrita()
    continuar = input("Continuar?")
    if continuar == "N":
        break