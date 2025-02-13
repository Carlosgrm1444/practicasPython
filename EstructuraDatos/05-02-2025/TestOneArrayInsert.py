from array import array

def insert(arrays, value, insertIndex):
    length = len(arrays)
    tempArray = array("i", [0] * (length + 1))  # ? Crea un array más grande

    for i in range(length):
        if i < insertIndex:
            tempArray[i] = arrays[i]  # ? Copia los elementos antes de insertIndex
        else:
            tempArray[i + 1] = arrays[i]  # ? Mueve los elementos hacia la derecha

    tempArray[insertIndex] = value  # ? Inserta el nuevo valor en la posición correcta
    return tempArray  # ? Devuelve el nuevo array fuera del bucle

def main():
    arrays = array('i', [90, 70, 50, 80, 60, 85])
    new_array = insert(arrays, 75, 2)  # ? Inserta 75 en la posición 2

    for i in new_array:
        print(i, ",", end="")

if __name__ == "__main__":
    main()
