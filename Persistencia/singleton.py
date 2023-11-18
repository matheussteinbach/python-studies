

class Controlador():
    __instancia = None

    def __init__(self):
        self.lista = []

    def __new__(cls):
        if Controlador.__instancia is None:
            Controlador.__instancia = object.__new__(cls)
        return Controlador.__instancia

controlador1 = Controlador()
controlador2 = Controlador()
controlador1.lista.append('Item 1')
controlador2.lista.append('Item 2')

print(controlador1.lista)
print(controlador2.lista)
print(controlador1)
print(controlador2)