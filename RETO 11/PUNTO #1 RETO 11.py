def pedir_matriz(nombre):
    matriz = []
    f = int(input(f"Ingrese el número de filas de la matriz {nombre}: "))
    c = int(input(f"Ingrese el número de columnas de la matriz {nombre}: "))
    for i in range(f):
        fila = []
        for j in range(c):
            valor = int(input(f"Ingrese el valor de la posición ({i}, {j}) de la matriz {nombre}: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumar_matrices(m1, m2):
    resultado = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            fila.append(m1[i][j] + m2[i][j])
        resultado.append(fila)
    return resultado

def restar_matrices(m1, m2):
    resultado = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            fila.append(m1[i][j] - m2[i][j])
        resultado.append(fila)
    return resultado

# Pedimos al usuario que ingrese las matrices
m1 = pedir_matriz("1")
m2 = pedir_matriz("2")

# Imprimimos las matrices originales
print("Matriz 1:")
for fila in m1:
    print(fila)

print("Matriz 2:")
for fila in m2:
    print(fila)

# Verificamos que ambas matrices tengan las mismas dimensiones
if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
    print("Las matrices no tienen las mismas dimensiones por lo cual no pueden sumarse o restarse")
else:
    # Sumamos las matrices
    resultado_suma = sumar_matrices(m1, m2)
    
    # Imprimimos la matriz resultante de la suma
    print("Resultado de la suma:")
    for fila in resultado_suma:
        print(fila)
    
    # Restamos las matrices
    resultado_resta = restar_matrices(m1, m2)
    
    # Imprimimos la matriz resultante de la resta
    print("Resultado de la resta:")
    for fila in resultado_resta:
        print(fila)