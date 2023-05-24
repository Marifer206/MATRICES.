# :star: MATRICES :star:
## Un dia nuevo, un nuevo reto
REALIZANDO NUESTRO RETO #11

## PUNTOS DEL RETO
### :round_pushpin: PUNTO #1 
+  Desarrolle un programa que permita realizar la [suma/resta de matrices](https://es.wikipedia.org/wiki/Adici%C3%B3n_matricial). El programa debe validar las condiciones necesarias para ejecutar la operación.

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
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
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/63N0zNPn/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>


### :round_pushpin: PUNTO #2
+ Desarrolle un programa que permita realizar el [producto de matrices](https://es.wikipedia.org/wiki/Multiplicaci%C3%B3n_de_matrices). El programa debe validar las condiciones necesarias para ejecutar la operación. 
    
#### :space_invader: CODIGO DEL PROGRAMA
```ruby
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

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/jS4PKJ3w/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #3  
+ Desarrolle un programa que permita obtener la  [matriz transpuesta](https://es.wikipedia.org/wiki/Matriz_transpuesta) de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
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
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/fT7zy7cK/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #4 
+ Desarrollar un programa que sume los elementos de una columna dada de una matriz.

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
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

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/139KNnMD/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

  
### :round_pushpin: PUNTO #5
+ Desarrollar un programa que sume los elementos de una fila dada de una matriz.

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
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
    print("La suma de los elementos de la fila " +  str(columna) + " es: " + str(resultado_suma))

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/KjZ9NyW4/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>


## :sparkles: Esto es todo hoy amigos :blush:, espero poder haberlos ayudado he inspirado para encontar nuevas solociones para nuevos retos :sparkles: 
