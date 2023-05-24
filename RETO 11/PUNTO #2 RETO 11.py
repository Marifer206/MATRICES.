def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingrese el valor de la posición ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def validar_multiplicacion(m1, m2):
    c1 = len(m1[0])
    f2 = len(m2)
    if c1 != f2:
        return False
    else:
        return True

def producto_matrices(m1, m2):
    f1 = len(m1)
    c2 = len(m2[0])
    resultado = [[0] * c2 for i in range(f1)]
    for i in range(f1):
        for j in range(c2):
            for k in range(len(m2)):
                resultado[i][j] += m1[i][k] * m2[k][j]
    return resultado

# Pedimos al usuario que ingrese las matrices
f1 = int(input("Ingrese el número de filas de la primera matriz: "))
c1 = int(input("Ingrese el número de columnas de la primera matriz: "))
m1 = crear_matriz(f1, c1)

f2 = int(input("Ingrese el número de filas de la segunda matriz: "))
c2 = int(input("Ingrese el número de columnas de la segunda matriz: "))
m2 = crear_matriz(f2, c2)

# Imprimimos las matrices originales
print("Matriz 1:")
for fila in m1:
    print(fila)

print("Matriz 2:")
for fila in m2:
    print(fila)

# Validamos las matrices
if not validar_multiplicacion(m1, m2):
    print("INVALIDO: el número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz")
else:
    # Realizamos el producto de matrices
    resultado = producto_matrices(m1, m2)
    
    # Imprimimos la matriz resultante
    print("Resultado del producto:")
    for fila in resultado:
        print(fila)