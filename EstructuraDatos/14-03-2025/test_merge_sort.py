# # * 14 de marzo de 2025

# # ? Carlos Gabriel Rodriguez Macias

# # ! El siguiente código implementa el algoritmo de ordenamiento Merge Sort.
# # ! Merge Sort es un algoritmo de ordenamiento eficiente que sigue el enfoque de "dividir y conquistar".
# # ! El código consta de tres funciones principales: `sort`, `merge_sort` y `merge`.
# # ! La función `sort` inicia el proceso de ordenamiento.
# # ! La función `merge_sort` divide el array en mitades y las ordena recursivamente.
# # ! La función `merge` combina dos mitades ordenadas en un solo array ordenado.
# # ! Al final, se prueba el algoritmo con un array de enteros.

from array import array  # ? Importa la clase `array` del módulo `array`.


# # * Función principal para iniciar el ordenamiento ##############################################
def sort(array):
    length = len(array)
    temp = [0] * length  # ? Array temporal para almacenar los valores ordenados.
    merge_sort(array, temp, 0, length - 1)  # ? Llama a la función merge_sort para ordenar el array.


# # * Función recursiva para dividir y ordenar el array ###########################################
def merge_sort(array, temp, left, right):
    if left < right:
        center = (left + right) // 2  # ? Encuentra el punto medio del array.
        merge_sort(array, temp, left, center)  # ? Ordena recursivamente la mitad izquierda.
        merge_sort(array, temp, center + 1, right)  # ? Ordena recursivamente la mitad derecha.
        merge(array, temp, left, center + 1, right)  # ? Combina las dos mitades ordenadas.


# # * Función para combinar dos mitades ordenadas #################################################
def merge(array, temp, left, right, rightEndIndex):
    leftEndIndex = right - 1  # ? Índice final de la mitad izquierda.
    tempIndex = left  # ? Índice inicial para el array temporal.
    elementNumber = rightEndIndex - left + 1  # ? Número total de elementos a combinar.

    # ? Combinar las dos mitades ordenadas.
    while left <= leftEndIndex and right <= rightEndIndex:
        if array[left] <= array[right]:
            temp[tempIndex] = array[left]  # ? Copia el elemento de la mitad izquierda.
            left += 1
        else:
            temp[tempIndex] = array[right]  # ? Copia el elemento de la mitad derecha.
            right += 1
        tempIndex += 1

    # ? Copiar los elementos restantes de la mitad izquierda (si los hay).
    while left <= leftEndIndex:
        temp[tempIndex] = array[left]
        left += 1
        tempIndex += 1

    # ? Copiar los elementos restantes de la mitad derecha (si los hay).
    while right <= rightEndIndex:
        temp[tempIndex] = array[right]
        right += 1
        tempIndex += 1

    # ? Copiar los elementos ordenados de temp de vuelta a array.
    for i in range(elementNumber):
        array[rightEndIndex] = temp[rightEndIndex]
        rightEndIndex -= 1


# # * Función principal para probar el algoritmo ##################################################
def main():
    scores = array("i", [50, 65, 99, 87, 74, 63, 76, 100, 92])  # ? Crea un array de tipo int.
    sort(scores)  # ? Ordena el array usando Merge Sort.
    for score in scores:
        print(score, ",", end="")  # ? Imprime los elementos ordenados.


if __name__ == "__main__":
    main()  # ? Ejecuta la función principal si el script es el programa principal.