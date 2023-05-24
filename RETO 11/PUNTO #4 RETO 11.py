# Definimos una función para sumar los elementos de una columna dada de una matriz
def sumar_columna(matriz, columna):
    # Verificamos que la columna sea válida
    if columna < 0 or columna >= len(matriz[0]):
        print("Error: la columna ingresada no es válida")
        return None
    
    # Sumamos los elementos de la columna
    suma = 0
    for fila in matriz:
        suma += fila[columna]
    
    # Devolvemos la suma
    return suma

# Pedimos al usuario que ingrese la matriz
matriz = []

filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese el valor de la posición ({i}, {j}) de la matriz: "))
        fila.append(valor)
    matriz.append(fila)

# Imprimimos la matriz
print("Matriz:")
for fila in matriz:
    print(fila)

# Pedimos al usuario que ingrese la columna a sumar
columna = int(input("Ingrese el número de la columna a sumar: 0 para la primera, 1 para la segunda, 2 para la tercera y asi sucesivamente: "))

# Sumamos los elementos de la columna
resultado_suma = sumar_columna(matriz, columna)

# Imprimimos el resultado
if resultado_suma != None:
    print("La suma de los elementos de la columna " +  str(columna) + " es: " + str(resultado_suma))