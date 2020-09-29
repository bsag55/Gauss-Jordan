# Método de resolución de sistemas de ecuaciones Gauss - Jordan

print('Método de resolución de sistemas de ecuaciones Gauss - Jordan')
print()

#  --- Sección de Métodos ---  #

def definir_filas():
    while True:
        try:
            x = int(input('Ingrese el número de filas de la matriz (recuerde ingresar valores positivos y enteros): '))
            assert (x > 0) and (type(x) == int)
            break
        except ValueError:
            print('Error: Dato incorrecto, por favor intente de nuevo: ')
            continue
        except AssertionError:
            print('Error: El número indicado es cero o negativo, por favor intente de nuevo: ')
            continue
    return x

def definir_columnas():
    while True:
        try:
            x = int(input('Ingrese el número de columnas de la matriz (recuerde ingresar valores positivos y enteros): '))
            assert (x > 0) and (type(x) == int)
            break
        except ValueError:
            print('Error: Dato incorrecto, por favor intente de nuevo: ')
            continue
        except AssertionError:
            print('Error: El número indicado es cero o negativo, por favor intente de nuevo: ')
            continue
    return x

def crear_matriz(filas, columnas):
    Matriz = [[None] * columnas for i in range(filas)]
    Matriz = np.array(Matriz, dtype='float')
    return Matriz

def llenar_matriz(filas,columnas,matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            x = float(input('Ingrese el numero de la fila ' + str(i + 1) + ' , y de la columna: ' + str(j + 1)) + '  ')
            Matriz[i][j] = x
    return Matriz

def comprobar_tamano(filas,columnas):
    if filas != columnas:
        print('La matriz no es cuadrada, no es posible ejecutar el procedimiento.')
        sys.exit()
    else:
        print('La matriz es cuadrada, el ejercicio puede continuar')
    
def comprobar_singular(matriz):
    if (round(np.linalg.det(matriz),2)) == 0:
        print('La matriz ingresada es singular, por lo tanto no se puede realizar el procedimeinto')
        sys.exit()
    else:
        print ('La matriz no es singular, el ejercicio puede continuar')

def vector_solucion(matriz):
    vector = [[None] for i in range(len(matriz))]
    vector = np.array(vector, dtype='float')
    for i in range(len(matriz)):
        x = float(input('Ingrese a qué es igual la ecuación ' + str(i + 1) + ' :  '))
        vector[i] = x
    matriz = np.append(matriz,vector,axis= 1)
    return matriz

def gauss_jordan(matriz):
    #Gauss - Jordan
    for i in range(len(matriz)):
        if matriz[i][i] == 0.0:
            print('División por cero')
            sys.exit()
            
        for j in range(len(matriz)):
            if i != j:
                ratio = matriz[j][i]/matriz[i][i]
                for k in range(len(matriz) + 1):
                    matriz[j][k] = matriz[j][k] - ratio * matriz[i][k]
    
    for i in range(len(matriz)):
        matriz[i] = matriz[i][len(matriz)]/matriz[i][i]

    # Mostrando la solución
    print('\nLa solución al sistema descrito en la matriz es: ')
    for i in range(len(matriz)):
        print(matriz[i][i], end = '\t')
        
        
#  --- Sección del programa ---  #
                    
# El usuario ingresa la dimensión de la matriz

filas = definir_filas()
columnas = definir_columnas()

# Se crea la matriz

Matriz = crear_matriz(filas,columnas)

# Se ingresan los valores a la matriz

llenar_matriz(filas,columnas,Matriz)

# Se validan las condiciones para poder ejecutar el método

comprobar_tamano(filas,columnas)
comprobar_singular(Matriz)

# Se añade el vector solución a la matriz

Matriz = vector_solucion(Matriz)

# Se imprime la Matriz
print()
print(Matriz)
print()

# Se implementa el método Gauss - Jordan

Matriz2 = Matriz.copy()
gauss_jordan(Matriz2)

# Por : Ing Brayan Alfonso.