# Definimos función para sumar los elementos de una fila dada de una matriz
def sumar_fila(matriz, fila):
    # Verificamos que la fila sea válida
    if fila < 0 or fila >= len(matriz):
        print("Error: la fila ingresada no es válida")
        return None
    
    # Sumamos los elementos de la fila
    suma = 0
    for elemento in matriz[fila]:
        suma += elemento
    
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

# Pedimos al usuario que ingrese la fila a sumar
fila = int(input("Ingrese el número de la fila a sumar: 0 para la primera, 1 para la segunda, 2 para la tercera y asi sucesivamente: "))

# Sumamos los elementos de la fila
resultado_suma = sumar_fila(matriz, fila)

# Imprimimos el resultado
if resultado_suma != None:
    print("La suma de los elementos de la fila " +  str(fila) + " es: " + str(resultado_suma))