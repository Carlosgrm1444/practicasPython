# # * 27 de febrero de 2025

# # ? Carlos Gabriel Rodriguez Macias

# # ! El siguiente código implementa una cola (Queue) utilizando una lista doblemente enlazada.
# # ! La cola es una estructura de datos que sigue el principio FIFO (First In, First Out).
# # ! Esto significa que el primer elemento en entrar es el primero en salir.
# # ! La cola tiene dos operaciones principales: `offer` (añadir un elemento) y `poll` (eliminar y obtener el primer elemento).
# # ! Además, se incluye una función para imprimir la cola y mostrar su contenido.


# # * Clase del Nodo para crear los siguientes objetos #############################################
class Node:
    # ? la clase cuenta con dos datos, el nombre del nodo y el siguiente nodo
    name = ""
    prev = None
    next = None

    # ? funcion de inicio del objeto
    def __init__(self, name):
        self.name = name


# # * Clase de la cola para crear los siguientes objetos ###########################################
class Queue:
    # ? La clase Queue representa una cola implementada con una lista doblemente enlazada.
    # ? Tiene tres atributos: la cabeza (head), la cola (tail) y el tamaño (size).
    __head = None
    __tail = None
    __size = 0

    # ? Método para añadir un elemento a la cola (operación `offer`).
    def offer(self, element):
        if self.__head == None:
            # ? Si la cola está vacía, el nuevo nodo se convierte en la cabeza y la cola.
            self.__head = Node(element)
            self.__tail = self.__head
        else:
            # ? Si la cola no está vacía, el nuevo nodo se añade al final (tail).
            new_node = Node(element)
            new_node.next = self.__tail
            self.__tail.prev = new_node
            self.__tail = new_node
        self.__size += 1  # ? Incrementa el tamaño de la cola.

    # ? Método para eliminar y obtener el primer elemento de la cola (operación `poll`).
    def poll(self):
        p = self.__head
        if p == None:
            # ? Si la cola está vacía, retorna None.
            return None
        # ? Mueve la cabeza al nodo anterior y desconecta el nodo eliminado.
        self.__head = self.__head.prev
        p.next = None
        p.prev = None
        self.__size -= 1  # ? Decrementa el tamaño de la cola.
        return p  # ? Retorna el nodo eliminado.

    # ? Propiedad para obtener el tamaño actual de la cola.
    @property
    def size(self):
        return self.__size

    # ? Método para imprimir la cola desde la cabeza hasta la cola.
    def output(self, queue):
        print("Head", end=" ")
        node = queue.poll()  # ? Obtiene y elimina el primer nodo.
        while node != None:
            # ? Imprime el nombre del nodo y obtiene el siguiente.
            print(node.name, "<-", end=" ")
            node = queue.poll()
        print("Tail\n")  # ? Indica el final de la cola.


# # * Función principal para probar la cola ########################################################
def main():
    # ? Crea una instancia de la cola.
    queue = Queue()

    # ? Añade elementos a la cola.
    queue.offer("A")
    queue.offer("B")
    queue.offer("C")
    queue.offer("D")

    # ? Imprime la cola.
    queue.output(queue)


# ? Punto de entrada del programa.
if __name__ == "__main__":
    main()
