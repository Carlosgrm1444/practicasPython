# # * 14 de marzo de 2025

# # ? Carlos Gabriel Rodriguez Macias

# # ! El siguiente código implementa el algoritmo de ordenamiento Quick Sort.
# # ! Quick Sort es un algoritmo de ordenamiento eficiente que sigue el enfoque de "dividir y conquistar".
# # ! El código consta de dos funciones principales: `sort` y `quick_sort`.
# # ! La función `sort` inicia el proceso de ordenamiento.
# # ! La función `quick_sort` divide el array en particiones y las ordena recursivamente.
# # ! Al final, se prueba el algoritmo con un array de enteros.

from array import array  # ? Importa la clase `array` del módulo `array`.

# # * Función principal para iniciar el ordenamiento ##############################################
def sort(array):
    length = len(array)
    if length > 0:
        quick_sort(array, 0, length - 1)  # ? Llama a la función quick_sort para ordenar el array.


# # * Función recursiva para dividir y ordenar el array ###########################################
def quick_sort(array, low, high):
    if low >= high:
        return  # ? Si el subarray tiene 0 o 1 elemento, termina la recursión.

    i = low  # ? Índice inicial para la partición izquierda.
    j = high  # ? Índice inicial para la partición derecha.
    threshold = array[low]  # ? Selecciona el pivote (primer elemento del subarray).

    while i < j:
        # ? Encuentra la primera posición inferior al umbral de derecha a izquierda.
        while i < j and array[j] > threshold:
            j -= 1
        # ? Reemplaza el elemento en la posición `i` con un número menor que el umbral.
        if i < j:
            array[i] = array[j]
            i += 1

        # ? Encuentra la primera posición mayor que el umbral de izquierda a derecha.
        while i < j and array[i] <= threshold:
            i += 1
        # ? Reemplaza el elemento en la posición `j` con un número mayor que el umbral.
        if i < j:
            array[j] = array[i]
            j -= 1

    # ? Coloca el umbral (pivote) en la posición correcta.
    array[i] = threshold

    # ? Ordena la parte izquierda del array (elementos menores que el pivote).
    quick_sort(array, low, i - 1)
    # ? Ordena la parte derecha del array (elementos mayores que el pivote).
    quick_sort(array, i + 1, high)


# # * Función principal para probar el algoritmo ##################################################
def main():
    scores = array("i", [90, 60, 50, 80, 70, 100])  # ? Crea un array de tipo int.
    sort(scores)  # ? Ordena el array usando Quick Sort.
    for score in scores:
        print(score, ", ", end="")  # ? Imprime los elementos ordenados.


if __name__ == "__main__":
    main()  # ? Ejecuta la función principal si el script es el programa principal.