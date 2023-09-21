
clientes = {"Pedro","Maria","Francisco"}
clientes2={"Pedro", "Ana","francisco"}
print(clientes)
print(clientes2)


print(" interseção entre o conjunto cliente e clientes2")
print(clientes.intersection(clientes2))
print("não altera o original:", clientes)


print("atualiza o original:")
clientes.intersection_update(clientes2)
print(clientes)

clientes3 = {"Karina", "Andressa", "Paulo", "Pedro"}
clientes.update(clientes3)
print(clientes)










