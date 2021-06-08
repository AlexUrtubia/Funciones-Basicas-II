# Cuenta regresiva : crea una función que acepte un número como entrada. 
# Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) 
# hasta 0 (como el último elemento).
# Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]
def cregresiva(a):
    nuevo = []
    for i in range (a, -1 , -1):
        nuevo.append(i)
    return nuevo
print(cregresiva(5))
# Imprimir y volver : crea una función que recibirá una lista con dos números. 
# #Imprima el primer valor y devuelva el segundo.
# Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2.
def print_and_return (a,b):
    print(a)
    return(b)
z = print_and_return(1,2)
print(z)
# First Plus Length : crea una función que acepta una lista y devuelve la suma del 
# primer valor de la lista más la longitud de la lista.
# Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)
def plus_length (a):
    return (a[0]+len(a))
z = plus_length([1,2,3,4,5])
print(z)
# Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista 
# que contenga solo los valores de la lista original que sean mayores que su segundo valor. 
# Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, 
# haga que la función devuelva False
# Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
# Ejemplo: values_greater_than_second ([3]) debería devolver False
def mayorquesdo (a):
    nueva = []
    if len(a) < 2:
        return False
    else:
        print ("El largo del array es: ",len(a))
        for i in range (0, len(a), 1):
            if a[i] > a[1]:
                nueva.append(a[i])
    return nueva
z = mayorquesdo([5,2,3,2,1,4])
print (z)
# Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
# La función debe crear y devolver una lista cuya longitud es igual al tamaño dado 
# y cuyos valores son todos los valores dados.
# Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
# Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]
def longval (a,b):
    aux = []
    for i in range (a):
        aux.append(b)
    return aux
z = longval(6,2)  
print(z)    