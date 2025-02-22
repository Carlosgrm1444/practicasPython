# # * 21 de febrero de 2025

# # ? Carlos Gabriel Rodriguez Macias

# # ! El siguiente codigo Crea dos clases y despues en base a ellas objetos
# # ! La primer clase son Nodos con el fin de usarse dentro de el segundo obj
# # ! Estos cuentan con tres valores, el nombre, el siguiente y anterior nodo
# # ! De ahi se deriba el nombre de listas doblemente enlazadas
# # ! El listado tiene una cabeza que es el nodo con el que comienza la Lista
# # ! Y tiene una cola que es el Nodo con el que termina la lista
# # ! Al final usa 3 funciones, add, insert y remove
# # ! Las cuales sus funciones son explicadas en el mismo codigo

# # * Clase del Nodo para crear los siguientes objetos #############################################
class Node:
    # ? la clase cuenta con dos datos, el nombre del nodo y el siguiente nodo
    name = ""
    prev = None
    next = None
    
    # ? funcion de inicio del objeto
    def __init__(self, name):
        self.name = name


# # * Clase del LinkedList para crear los siguientes objetos #######################################
class LinkedList:
    # ? tiene dos datos, la cabeza y la cola
    __head = None
    __tail = None

    def init(self):
        # ? asigna el nodo A a la cabeza
        self.__head = Node("A")
        self.__head.prev = None
        self.__head.next = None

        # ? crea y asigna el nodo B como siguiente de la caabeza (nodo A)
        nodeB = Node("B")
        nodeB.prev = self.__head
        nodeB.next = None
        self.__head.next = nodeB

        # ? Crea y asigna el nodo B como siguiente del nodo B
        nodeC = Node("C")
        nodeC.prev = nodeB
        nodeC.next = None
        nodeB.next = nodeC

        # ? Crea y asigna el nodo D como como la cola
        self.__tail = Node("D")
        self.__tail.prev = nodeC
        self.__tail.next = None
        nodeC.next = self.__tail

    # ? Funcion dentro del objeto para agregar un nuevo Nodo a la cola
    def add(self, newNode):
        self.__tail.next = newNode
        newNode.prev = self.__tail
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
        newNode.prev = p
        newNode.next.prev = newNode

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
        p.next.prev = p
        temp.next = None  # ? Eliminar nodo
        temp.prev = None  # ? Eliminar nodo

    @property
    def head(self):
        return self.__head


# # * Funcion para depurar el LinkedList y saber sus valore ########################################
def output(node):
    p = node
    end = None
    while p != None:  # ? Desde el principio hasta el final
        print(p.name, "->", end=" ")
        end = p
        p = p.next
    print("End\n")

    p = end
    while p != None:  # ? Desde el final hasta el principio
        print(p.name, "->", end=" ")
        p = p.prev
    print("Start\n\n")


def main():
    # ? Probamos el linkedList
    linkedList = LinkedList()
    linkedList.init()
    print("Default list")
    output(linkedList.head)

    # ? Agregamos un nuevo Nodo (Nodo E)
    print("list with add")
    linkedList.add(Node("E"))
    output(linkedList.head)

    # ? Insertamos un nuevo nodo en la posicion 3 (Nodo F)
    print("list with insert")
    linkedList.insert(
        3, Node("F")
    ) 
    output(linkedList.head)
    
    # ? Removemos el nodo de la posicion 3 (Nodo C)
    print("list with remove")
    linkedList.remove(2) 
    output(linkedList.head)

if __name__ == "__main__":
    main()
