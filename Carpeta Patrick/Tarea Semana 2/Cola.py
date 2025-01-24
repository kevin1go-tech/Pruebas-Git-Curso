class Cola:
    def __init__(self):
        self.cola = []

    def insertar(self, valor):
        self.cola.append(valor)

    def eliminar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)

    def mostrar(self):
        print(" -> ".join(map(str, self.cola)))

    def esta_vacia(self):
        return len(self.cola) == 0

# Ejemplo de uso
cola = Cola()
cola.insertar(1)
cola.insertar(2)
cola.insertar(3)
cola.mostrar()  # 1 -> 2 -> 3
cola.eliminar()
cola.mostrar()  # 2 -> 3
