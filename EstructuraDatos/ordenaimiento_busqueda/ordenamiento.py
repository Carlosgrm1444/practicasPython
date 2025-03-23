# # * Definimos una lista de ejemplo con valores desordenados
array_original = [64, 34, 25, 12, 22, 11, 90]


# * Función para imprimir el array
def print_array(array, nombre_algoritmo):
    print(f"Array ordenado con {nombre_algoritmo}: {array}")


# ! 1. Bubble Sort (Ordenamiento de Burbuja)
def bubble_sort(array):
    n = len(array)
    # ? Recorremos el array n veces
    for i in range(n):
        # ? Últimos i elementos ya están ordenados, no es necesario revisarlos
        for j in range(0, n - i - 1):
            # ? Si el elemento actual es mayor que el siguiente, los intercambiamos
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


# ! 2. Selection Sort (Ordenamiento por Selección)
def selection_sort(array):
    n = len(array)
    # ? Recorremos el array
    for i in range(n):
        # ? Suponemos que el índice actual es el mínimo
        indice_minimo = i
        # ? Buscamos el índice del elemento más pequeño en el resto del array
        for j in range(i + 1, n):
            if array[j] < array[indice_minimo]:
                indice_minimo = j
        # ? Intercambiamos el elemento actual con el mínimo encontrado
        array[i], array[indice_minimo] = array[indice_minimo], array[i]
    return array


# ! 3. Insertion Sort (Ordenamiento por Inserción)
def insertion_sort(array):
    # ? Recorremos el array desde el segundo elemento
    for i in range(1, len(array)):
        valor_actual = array[i]
        j = i - 1
        # ? Movemos los elementos mayores que el valor_actual a la derecha
        while j >= 0 and valor_actual < array[j]:
            array[j + 1] = array[j]
            j -= 1
        # ? Insertamos el valor_actual en su posición correcta
        array[j + 1] = valor_actual
    return array


# ! 4. Merge Sort (Ordenamiento por Mezcla)
def merge_sort(array):
    if len(array) > 1:
        # ? Dividimos el array en dos mitades
        mitad = len(array) // 2
        mitad_izquierda = array[:mitad]
        mitad_derecha = array[mitad:]

        # ? Ordenamos recursivamente ambas mitades
        merge_sort(mitad_izquierda)
        merge_sort(mitad_derecha)

        i = j = k = 0

        # ? Combinamos las dos mitades ordenadas
        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                array[k] = mitad_izquierda[i]
                i += 1
            else:
                array[k] = mitad_derecha[j]
                j += 1
            k += 1

        # ? Si quedan elementos en la mitad izquierda, los añadimos
        while i < len(mitad_izquierda):
            array[k] = mitad_izquierda[i]
            i += 1
            k += 1

        # ? Si quedan elementos en la mitad derecha, los añadimos
        while j < len(mitad_derecha):
            array[k] = mitad_derecha[j]
            j += 1
            k += 1
    return array


# ! 5. Quick Sort (Ordenamiento Rápido)
def quick_sort(array):
    if len(array) <= 1:
        return array
    # ? Elegimos un pivote (en este caso, el elemento del medio)
    pivote = array[len(array) // 2]
    # ? Dividimos el array en tres partes: menores, iguales y mayores que el pivote
    menores = [x for x in array if x < pivote]
    iguales = [x for x in array if x == pivote]
    mayores = [x for x in array if x > pivote]
    # ? Concatenamos las partes ordenadas
    return quick_sort(menores) + iguales + quick_sort(mayores)


# ! 6. Heap Sort (Ordenamiento por Montículos)
def heapify(array, n, i):
    # ? Inicializamos el índice del elemento más grande como la raíz
    indice_mas_grande = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    # ? Si el hijo izquierdo es mayor que la raíz
    if izquierda < n and array[i] < array[izquierda]:
        indice_mas_grande = izquierda

    # ? Si el hijo derecho es mayor que el más grande hasta ahora
    if derecha < n and array[indice_mas_grande] < array[derecha]:
        indice_mas_grande = derecha

    # ? Si el más grande no es la raíz, intercambiamos
    if indice_mas_grande != i:
        array[i], array[indice_mas_grande] = array[indice_mas_grande], array[i]
        # ? Aseguramos que el subárbol afectado siga siendo un montículo
        heapify(array, n, indice_mas_grande)


def heap_sort(array):
    n = len(array)
    # ? Construimos un montículo máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
    # ? Extraemos elementos uno por uno
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


# ! 7. Shell Sort (Ordenamiento de Shell)
def shell_sort(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            # ? Movemos los elementos mayores que temp a la derecha
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
    return array


# * Probamos cada algoritmo de ordenamiento
print("Array original:", array_original)

# ? Bubble Sort
array_bubble = bubble_sort(array_original.copy())
print_array(array_bubble, "Bubble Sort")

# ? Selection Sort
array_selection = selection_sort(array_original.copy())
print_array(array_selection, "Selection Sort")

# ? Insertion Sort
array_insertion = insertion_sort(array_original.copy())
print_array(array_insertion, "Insertion Sort")

# ? Merge Sort
array_merge = merge_sort(array_original.copy())
print_array(array_merge, "Merge Sort")

# ? Quick Sort
array_quick = quick_sort(array_original.copy())
print_array(array_quick, "Quick Sort")

# ? Heap Sort
array_heap = heap_sort(array_original.copy())
print_array(array_heap, "Heap Sort")

# ? Shell Sort
array_shell = shell_sort(array_original.copy())
print_array(array_shell, "Shell Sort")
