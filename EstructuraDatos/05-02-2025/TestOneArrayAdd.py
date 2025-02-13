from array import array

def add ( arrays, value):
    length = len(arrays)
    # ? Cree un tempArray mas grande que el del arreglo
    
    tempArray = array('i', [0 for _ in range(length + 1)])
    
    for i in range(0, length):
        tempArray[i] = arrays[i] # ? Copie el valor de la matriz a tmpArray
        
        tempArray[length] = value # ? Insertar valor en el ultimo indice de tempArray
            
    return tempArray

def main():
    # ? Crea una matriz de tipo int
    arrays = array('i', [90, 70, 50, 80, 60, 85])

    arrays =  add(arrays, 75)    
        
    length = len(arrays)
    for i in range(0, length):
        print(arrays[i], ",", end = "")
            
if __name__ == "__main__":
    main()
        
        