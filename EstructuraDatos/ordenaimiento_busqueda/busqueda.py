# # * Definimos una lista de ejemplo (debe estar ordenada para algunos algoritmos)
array_original = [11, 12, 22, 25, 34, 64, 90]


# * Función para imprimir el resultado de la búsqueda
def imprimir_resultado(indice, valor_buscado, nombre_algoritmo):
    if indice != -1:
        print(
            f"El valor {valor_buscado} fue encontrado en el índice {indice} usando {nombre_algoritmo}."
        )
    else:
        print(f"El valor {valor_buscado} no fue encontrado usando {nombre_algoritmo}.")


# ! 1. Búsqueda Lineal (Linear Search)
def busqueda_lineal(array, valor_buscado):
    # ? Recorremos el array elemento por elemento
    for i in range(len(array)):
        if array[i] == valor_buscado:
            return i  # ? Retornamos el índice si encontramos el valor
    return -1  # ? Retornamos -1 si no se encuentra el valor


# ! 2. Búsqueda Binaria (Binary Search)
def busqueda_binaria(array, valor_buscado):
    izquierda, derecha = 0, len(array) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if array[medio] == valor_buscado:
            return medio  # ? Retornamos el índice si encontramos el valor
        elif array[medio] < valor_buscado:
            izquierda = medio + 1  # ? Buscamos en la mitad derecha
        else:
            derecha = medio - 1  # ? Buscamos en la mitad izquierda
    return -1  # ? Retornamos -1 si no se encuentra el valor


# ! 3. Búsqueda por Saltos (Jump Search)
def busqueda_por_saltos(array, valor_buscado):
    n = len(array)
    paso = int(n**0.5)  # ? Tamaño del salto
    previo = 0

    # ? Buscamos el bloque donde podría estar el valor
    while array[min(paso, n) - 1] < valor_buscado:
        previo = paso
        paso += int(n**0.5)
        if previo >= n:
            return -1

    # ? Realizamos una búsqueda lineal dentro del bloque
    while array[previo] < valor_buscado:
        previo += 1
        if previo == min(paso, n):
            return -1

    if array[previo] == valor_buscado:
        return previo
    return -1


# ! 4. Búsqueda por Interpolación (Interpolation Search)
def busqueda_por_interpolacion(array, valor_buscado):
    izquierda, derecha = 0, len(array) - 1
    while izquierda <= derecha and array[izquierda] <= valor_buscado <= array[derecha]:
        # ? Fórmula de interpolación para estimar la posición
        posicion = izquierda + (
            (valor_buscado - array[izquierda]) * (derecha - izquierda)
        ) // (array[derecha] - array[izquierda])
        if array[posicion] == valor_buscado:
            return posicion
        elif array[posicion] < valor_buscado:
            izquierda = posicion + 1
        else:
            derecha = posicion - 1
    return -1


# ! 5. Búsqueda Exponencial (Exponential Search)
def busqueda_exponencial(array, valor_buscado):
    if array[0] == valor_buscado:
        return 0
    n = len(array)
    i = 1
    # ? Duplicamos el índice hasta encontrar un rango
    while i < n and array[i] <= valor_buscado:
        i *= 2
    # ? Realizamos una búsqueda binaria dentro del rango
    return busqueda_binaria(array[i // 2 : min(i, n)], valor_buscado) + (
        i // 2
        if busqueda_binaria(array[i // 2 : min(i, n)], valor_buscado) != -1
        else 0
    )


# ! 6. Búsqueda en Profundidad (DFS) para grafos
def dfs(grafo, inicio, valor_buscado, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    if inicio == valor_buscado:
        return inicio
    for vecino in grafo[inicio]:
        if vecino not in visitados:
            resultado = dfs(grafo, vecino, valor_buscado, visitados)
            if resultado != -1:
                return resultado
    return -1


# ! 7. Búsqueda en Anchura (BFS) para grafos
from collections import deque


def bfs(grafo, inicio, valor_buscado):
    cola = deque([inicio])
    visitados = set([inicio])
    while cola:
        nodo = cola.popleft()
        if nodo == valor_buscado:
            return nodo
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
    return -1


# * Probamos cada algoritmo de búsqueda
valor_buscado = 25
print("Array original:", array_original)

# ? Búsqueda Lineal
indice_lineal = busqueda_lineal(array_original, valor_buscado)
imprimir_resultado(indice_lineal, valor_buscado, "Búsqueda Lineal")

# ? Búsqueda Binaria
indice_binario = busqueda_binaria(array_original, valor_buscado)
imprimir_resultado(indice_binario, valor_buscado, "Búsqueda Binaria")

# ? Búsqueda por Saltos
indice_saltos = busqueda_por_saltos(array_original, valor_buscado)
imprimir_resultado(indice_saltos, valor_buscado, "Búsqueda por Saltos")

# ? Búsqueda por Interpolación
indice_interpolacion = busqueda_por_interpolacion(array_original, valor_buscado)
imprimir_resultado(indice_interpolacion, valor_buscado, "Búsqueda por Interpolación")

# ? Búsqueda Exponencial
indice_exponencial = busqueda_exponencial(array_original, valor_buscado)
imprimir_resultado(indice_exponencial, valor_buscado, "Búsqueda Exponencial")

# ? Búsqueda en Profundidad (DFS)
# * Definimos un grafo de ejemplo
grafo = {
    11: [12, 22],
    12: [11, 25],
    22: [11, 34],
    25: [12, 64],
    34: [22, 90],
    64: [25],
    90: [34],
}
indice_dfs = dfs(grafo, 11, valor_buscado)
imprimir_resultado(indice_dfs, valor_buscado, "Búsqueda en Profundidad (DFS)")

# ? Búsqueda en Anchura (BFS)
indice_bfs = bfs(grafo, 11, valor_buscado)
imprimir_resultado(indice_bfs, valor_buscado, "Búsqueda en Anchura (BFS)")
