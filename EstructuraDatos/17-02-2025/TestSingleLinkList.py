# # * 17 de febrero de 2025

# # ? Carlos Gabriel Rodriguez Macias

# # ! El siguiente codigo Crea dos clases y despues en base a ellas objetos
# # ! La primer clase son Nodos con el fin de usarse dentro de el segundo obj
# # ! Estos cuentan con dos valores, el nombre y el siguiente nodo
# # ! El listado tiene una cabeza que es el nodo con el que comienza la Lista
# # ! Y tiene una cola que es el Nodo con el que termina la lista
# # ! Al final usa 3 funciones, add, insert y remove
# # ! Las cuales sus funciones son explicadas en el mismo codigo

# # * Clase del Nodo para crear los siguientes objetos #############################################
class Node:
    # ? la clase cuenta con dos datos, el nombre del nodo y el siguiente nodo
    nombre = ""
    next = None

    # ? funcion de inicio del objeto
    def __init__(self, nombre, next):
        self.nombre = nombre
        self.next = next


# # * Clase del LinkedList para crear los siguientes objetos #######################################
class LinkedList:
    # ? tiene dos datos, la cabeza y la cola
    __head = None
    __tail = None

    def init(self):
        # ? asigna el nodo A a la cabeza
        self.__head = Node("A", None)

        # ? crea y asigna el nodo B como siguiente de la caabeza (nodo A)
        nodeB = Node("B", None)
        self.__head.next = nodeB

        # ? Crea y asigna el nodo B como siguiente del nodo B
        nodeC = Node("C", None)
        nodeB.next = nodeC

        # ? Crea y asigna el nodo D como como la cola
        self.__tail = Node("D", None)
        nodeC.next = self.__tail

    # ? Funcion dentro del objeto para agregar un nuevo Nodo a la cola
    def add(self, newNode):
        self.__tail.next = newNode
        self.__tail = newNode

    # ? Funcion dentro del objeto para insertar un nuevo Nodo en una posicion exacta
    def insert(self, insertPosition, newNode):
        p = self.__head
        i = 0
        # ? Mueva el nodo a la posicion de insercion
        while p.next != None and i < insertPosition - 1:
            p = p.next
            i += 1

        newNode.next = p.next
        p.next = newNode

    # ? Funcion dentro del objeto para remover un Nodo de una posicion exacta
    def remove(self, removePosition):
        p = self.__head
        i = 0
        # ? Mueva el nodo a la posicion del nodo anterior que desea eliminar
        while p.next != None and i < removePosition - 1:
            p = p.next
            i += 1
        temp = p.next  # ? Guarde el nodo que desea eliminar
        p.next = p.next.next
        temp.next = None  # ? Eliminar nodo

    @property
    def head(self):
        return self.__head


# # * Funcion para depurar el LinkedList y saber sus valore ########################################
def output(node):
    p = node
    while p != None:  # ? Desde el principio hasta el final
        nombre = p.nombre
        print(nombre, "->", end=" ")
        p = p.next
    print("End\n\n")


def main():
    # ? Probamos el linkedList
    linkedList = LinkedList()
    linkedList.init()
    output(linkedList.head)

    # ? Agregamos un nuevo Nodo (Nodo E)
    linkedList.add(Node("E", None))
    output(linkedList.head)

    # ? Insertamos un nuevo nodo en la posicion 3 (Nodo F)
    linkedList.insert(
        3, Node("F", None)
    ) 
    output(linkedList.head)
    
    # ? Removemos el nodo de la posicion 3 (Nodo C)
    linkedList.remove(2) 
    output(linkedList.head)


if __name__ == "__main__":
    main()
