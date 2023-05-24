# Definimos una función para obtener la matriz transpuesta
def matriz_transpuesta(m):
    # Creamos una matriz vacía para almacenar el resultado
    resultado = []
    
    # Recorremos las columnas de la matriz original
    for j in range(len(m[0])):
        fila = []
        # Recorremos las filas de la matriz original
        for i in range(len(m)):
            # Agregamos el valor de la celda (i,j) a la nueva fila
            fila.append(m[i][j])
        resultado.append(fila)
    
    # Devolvemos la matriz transpuesta
    return resultado

# Pedimos al usuario que ingrese la matriz
m = []

f = int(input("Ingrese el número de filas de la matriz: "))
c = int(input("Ingrese el número de columnas de la matriz: "))

for i in range(f):
    fila = []
    for j in range(c):
        valor = int(input(f"Ingrese el valor de la posición ({i}, {j}) de la matriz: "))
        fila.append(valor)
    m.append(fila)

# Imprimimos la matriz original
print("Matriz original:")
for fila in m:
    print(fila)

# Obtenemos la matriz transpuesta
resultado_transpuesta = matriz_transpuesta(m)

# Imprimimos la matriz transpuesta
if resultado_transpuesta != None:
    print("Matriz transpuesta:")
    for fila in resultado_transpuesta:
        print(fila)