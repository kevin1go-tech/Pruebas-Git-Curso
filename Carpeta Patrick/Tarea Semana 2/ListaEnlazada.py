class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.head:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar(self, valor):
        if not self.head:
            return
        if self.head.valor == valor:
            self.head = self.head.siguiente
            return
        actual = self.head
        while actual.siguiente and actual.siguiente.valor != valor:
            actual = actual.siguiente
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente

    def mostrar(self):
        actual = self.head
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.mostrar()  # 1 -> 2 -> 3 -> None
lista.eliminar(2)
lista.mostrar()  # 1 -> 3 -> None
