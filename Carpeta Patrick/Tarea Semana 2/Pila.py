class Pila:
    def __init__(self):
        self.pila = []

    def insertar(self, valor):
        self.pila.append(valor)

    def eliminar(self):
        if not self.esta_vacia():
            return self.pila.pop()

    def mostrar(self):
        print(" -> ".join(map(str, self.pila)))

    def esta_vacia(self):
        return len(self.pila) == 0

# Ejemplo de uso
pila = Pila()
pila.insertar(1)
pila.insertar(2)
pila.insertar(3)
pila.mostrar()  # 1 -> 2 -> 3
pila.eliminar()
pila.mostrar()  # 1 -> 2
