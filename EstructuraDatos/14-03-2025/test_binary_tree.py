# # * 14 de marzo de 2025

# # ? Carlos Gabriel Rodriguez Macias

# # ! El siguiente código crea dos clases y luego, en base a ellas, objetos.
# # ! La primera clase es `Node`, que representa un nodo en un árbol binario.
# # ! Cada nodo tiene tres valores: el dato que almacena, el nodo izquierdo y el nodo derecho.
# # ! La segunda clase es `BinaryTree`, que representa un árbol binario de búsqueda.
# # ! El árbol tiene una raíz (`_root`), que es el nodo principal del árbol.
# # ! Al final, se usan dos funciones principales: `insert` para agregar nodos y `inOrder` para recorrer el árbol.
# # ! Las funciones están explicadas en el mismo código.


# # * Clase del Nodo para crear los siguientes objetos #############################################
class Node:
    # ? La clase cuenta con tres datos: el valor del nodo, el nodo izquierdo y el nodo derecho.
    def __init__(self, data, left, right):
        self.data = data  # ? Valor almacenado en el nodo.
        self.left = left  # ? Referencia al nodo izquierdo.
        self.right = right  # ? Referencia al nodo derecho.


# # * Clase del BinaryTree para crear los siguientes objetos #######################################
class BinaryTree:
    def __init__(self):
        self._root = None  # ? La raíz del árbol, inicialmente vacía.

    @property
    def root(self):
        return self._root  # ? Propiedad para obtener la raíz del árbol.

    # ? Función para recorrer el árbol en orden (in-order traversal).
    def inOrder(self, root):
        if root is None:
            return  # ? Si el nodo es nulo, termina la recursión.
        self.inOrder(root.left)  # ? Recorre recursivamente el subárbol izquierdo.
        print(root.data, ",", end="")  # ? Imprime el valor del nodo actual.
        self.inOrder(root.right)  # ? Recorre recursivamente el subárbol derecho.

    # ? Función para insertar un nuevo nodo en el árbol.
    def insert(self, node, new_data):
        if self._root is None:
            self._root = Node(
                new_data, None, None
            )  # ? Si el árbol está vacío, crea la raíz.
            return

        compareValue = (
            new_data - node.data
        )  # ? Compara el nuevo dato con el dato del nodo actual.
        # ? Subárbol izquierdo recursivo, continúa buscando la posición de inserción.
        if compareValue < 0:
            if node.left is None:
                node.left = Node(
                    new_data, None, None
                )  # ? Inserta el nuevo nodo a la izquierda.
            else:
                self.insert(
                    node.left, new_data
                )  # ? Recursión en el subárbol izquierdo.
        elif compareValue > 0:
            # ? Subárbol derecho recursivo para encontrar la posición de inserción.
            if node.right is None:
                node.right = Node(
                    new_data, None, None
                )  # ? Inserta el nuevo nodo a la derecha.
            else:
                self.insert(node.right, new_data)  # ? Recursión en el subárbol derecho.


# # * Función principal para probar el BinaryTree #################################################
def main():
    binary_tree = BinaryTree()  # ? Crea un nuevo árbol binario.
    # ? Construyendo un árbol de búsqueda binario.
    binary_tree.insert(binary_tree.root, 60)
    binary_tree.insert(binary_tree.root, 40)
    binary_tree.insert(binary_tree.root, 20)
    binary_tree.insert(binary_tree.root, 10)
    binary_tree.insert(binary_tree.root, 30)
    binary_tree.insert(binary_tree.root, 50)
    binary_tree.insert(binary_tree.root, 80)
    binary_tree.insert(binary_tree.root, 70)
    binary_tree.insert(binary_tree.root, 90)

    print("\nin-order traversal binary search tree")
    binary_tree.inOrder(
        binary_tree.root
    )  # ? Recorre el árbol en orden y muestra los valores.


if __name__ == "__main__":
    main()  # ? Ejecuta la función principal si el script es el programa principal.
