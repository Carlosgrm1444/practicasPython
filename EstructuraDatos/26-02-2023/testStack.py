# # * 27 de febrero de 2025

# # ? Carlos Gabriel Rodriguez Macias

# # ! El siguiente código implementa una pila (Stack) utilizando una lista enlazada.
# # ! La pila es una estructura de datos que sigue el principio LIFO (Last In, First Out).
# # ! Esto significa que el último elemento en entrar es el primero en salir.
# # ! La pila tiene dos operaciones principales: `push` (añadir un elemento) y `pop` (eliminar y obtener el último elemento).
# # ! Además, se incluye una función para imprimir la pila y mostrar su contenido.

# # * Clase del Nodo para crear los siguientes objetos #############################################
class Node:
    # ? La clase Node representa un nodo en la lista enlazada.
    # ? Cada nodo tiene dos atributos: el nombre (name) y el nodo siguiente (next).
    name = ""
    next = None

    # ? Función de inicio del objeto. Inicializa el nodo con un nombre.
    def __init__(self, name):
        self.name = name


# # * Clase de la pila para crear los siguientes objetos ###########################################
class Stack:
    # ? La clase Stack representa una pila implementada con una lista enlazada.
    # ? Tiene dos atributos: el tope (top) y el tamaño (size).
    __top = None
    __size = 0

    # ? Método para añadir un elemento a la pila (operación `push`).
    def push(self, element):
        if self.__top == None:
            # ? Si la pila está vacía, el nuevo nodo se convierte en el tope.
            self.__top = Node(element)
        else:
            # ? Si la pila no está vacía, el nuevo nodo se añade al tope.
            new_node = Node(element)
            new_node.next = self.__top
            self.__top = new_node
        self.__size += 1  # ? Incrementa el tamaño de la pila.

    # ? Método para eliminar y obtener el último elemento de la pila (operación `pop`).
    def pop(self):
        if self.__top == None:
            # ? Si la pila está vacía, retorna None.
            return None
        p = self.__top
        # ? Mueve el tope al nodo siguiente y desconecta el nodo eliminado.
        self.__top = self.__top.next
        p.next = None
        self.__size -= 1  # ? Decrementa el tamaño de la pila.
        return p  # ? Retorna el nodo eliminado.

    # ? Propiedad para obtener el tamaño actual de la pila.
    @property
    def size(self):
        return self.__size

    # ? Método para imprimir la pila desde el tope hasta el final.
    def output(self, stack):
        print("Top", end=" ")
        node = stack.pop()  # ? Obtiene y elimina el último nodo.
        while node != None:
            # ? Imprime el nombre del nodo y obtiene el siguiente.
            print(node.name, "->", end=" ")
            node = stack.pop()
        print("End\n")  # ? Indica el final de la pila.


# # * Función principal para probar la pila ########################################################
def main():
    # ? Crea una instancia de la pila.
    stack = Stack()

    # ? Añade elementos a la pila.
    stack.push("A")
    stack.push("B")
    stack.push("C")
    stack.push("D")

    # ? Imprime la pila.
    stack.output(stack)


# ? Punto de entrada del programa.
if __name__ == "__main__":
    main()