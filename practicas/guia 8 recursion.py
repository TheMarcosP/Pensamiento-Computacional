# %%
# 1. ★☆☆ Para cada inciso, implementá una función recursiva que reciba un número z y un entero k y
# retorne:
# 1. z + k (sumando unos),
# 2. z * k (sumas sucesivas), y
# 3. z ^ k (multiplicaciones sucesivas)
from re import X


def suma_recursiva(z,k):
    if z != 0:
        return suma_recursiva(z-1,k) + 1
    if k != 0:
        return suma_recursiva(z,k-1) + 1
    else:
        return 0

print("test suma recursiva")
print("suma recursiva 1 + 1 = ", suma_recursiva(1,1))
print("suma recursiva 10 + 20 = ", suma_recursiva(10,20))

# 5*6 = 6 + 6 + 6 + 6 + 6 
def multi_recursiva(z,k):
    if z != 0:
        return multi_recursiva(z-1,k) + k
    else:
        return 0

print("test multi recursiva")
print("multi recursiva 0 * 0 = ", multi_recursiva(0,0))
print("multi recursiva 0 * 1 = ", multi_recursiva(0,1))
print("multi recursiva 1 * 0 = ", multi_recursiva(1,0))
print("multi recursiva 1 * 1 = ", multi_recursiva(1,1))
print("multi recursiva 1 * 2 = ", multi_recursiva(1,2))
print("multi recursiva 10 * 20 = ", multi_recursiva(10,20))


# z^k = z*z*z... k veces

# 1c ingenuo 
def pwr_recursiva(z,k):
    if k == 0:
        return 1
    elif k == 1:
        return z
    else:
        return pwr_recursiva(multi_recursiva(z,z),k-1)
    

# 1c piola
def pot(a,k):
    if k == 0:
        return 1
    elif k == 1:
        return a
    pa2 = pot(a,k//2) # a^5 = a^2 * a^2 * a
    pa2 *= pa2
    if k%2:
        pa2 *= a
    return pa2

# %%
# 2. ★☆☆ Implementar una función recursiva que retorne la cantidad de dígitos de un número entero.

def len_digits(n):
    if n == 0:
        return 0
    return len_digits(n//10) + 1

print("test len digits")
print("len digits 0 = ", len_digits(0))
print("len digits 1 = ", len_digits(1))
print("len digits 10 = ", len_digits(17))
print("len digits 100 = ", len_digits(145))



# %%
#3. ★☆☆ Implementar una función recursiva que reciba un entero no negativo e retorne dicho número
# espejado, es decir, para el 1234 retorna 4321.


def espejado(num):
    s = str(num)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))


print("test espejado")
print("espejado 0 = ", espejado(0))
print("espejado 1 = ", espejado(1))
print("espejado 12 = ", espejado(12))
print("espejado 123 = ", espejado(123))


#%%
# 4. ★☆☆ Escribir una función recursiva que calcule el n-ésimo número triangular (el número triangular de
# n es 1 + 2 + 3 + ··· + n)

def num_triangular(n):
    # print(n)
    if n == 0:
        return 0
    return num_triangular(n-1) + n

print("test num triangular")
print("num triangular 0 = ", num_triangular(0))
print("num triangular 1 = ", num_triangular(1))
print("num triangular 2 = ", num_triangular(2))
print("num triangular 40 = ", num_triangular(40))

# %%

# 5. ★★☆ Implementar una función recursiva que dados dos números n y b retorne True si n es potencia
# de b.

# es potencia si, para algun k,  n = b^k 
# osea n = b*b*b... k veces
#ej 100 = 10^2
#ej 32 = 2^5
#ej 1 = 1^1
#ej 0 = 0^0
#ej 0 != 1^k para cualquier k
def is_pwr(n,b):
    'funciona solo para positivos'
    if b == 1 and n != 1 or b == 0 and n != 0:
        return False
    if n < b:
        return False
    elif n == b:
        return True
    return is_pwr(n/b,b)

#%%
# 6. ★★☆ Escribir una función recursiva que encuentre el mayor elemento de un vector

def max_vector(vector : list):
    if len(vector) == 1:
        return vector[0]
    if vector[0] > vector[1]:
        vector.pop(1)
    else:
        vector.pop(0)
    return max_vector(vector)

print("test max vector")
print("max vector [0] = ", max_vector([0]))
print("max vector [1] = ", max_vector([1]))
print("max vector [1,2] = ", max_vector([1,2]))
print("max vector [2,1] = ", max_vector([2,1]))
print("max vector [1,2,3] = ", max_vector([1,2,3]))

# %%

# 7. ★★☆ Escribir una función recursiva que calcule el n-ésimo número de la sucesión de Fibonacci. La
# misma se define como F_n = F_{n-1} + F_{n-2}, F_0 = F_1 = 1.
# Dibuje un esquema (árbol de recursividad) de las llamadas recursivas para n = 6.

def recursive_fibonacci(n):
    if n <= 1:
        return 1
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

# secuencia de fibonacci 
# 1 2 3 4 5 6 7  8  9  10 11 12 13 14


# %%

# segunda opcion
#algoritmo de euclides
def gcd(m,n):
    if n == 0:
        return m
    return gcd(n,m%n)

# #tercer opcion
# def gcd(m,n):
#     if m == n:
#         return m
#     if m>n:
#         return gcd(m,n-m)
    

print("test gcd")
print("gcd 0,0 = ", gcd(0,0))
print("gcd 1,0 = ", gcd(1,0))
print("gcd 20,5 = ", gcd(20,5))
print("gcd 36,12 = ", gcd(36,12))

# %%

# 9. ★★☆ Escribir una función recursiva que dado un arreglo de números, retorne el máximo, usando
# dividir y conquistar

def max_n(n:list):
    print(n)
    if len(n) == 1:
        return n[0]
    elif len(n) == 2:
        return n[0] if n[0] >= n[1] else n[1]
    else:
        sep = len(n)//2
        return max_n(max_n(n[:sep]), max_n(n[sep:]))
    
# 10 El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera:

# Las filas se enumeran desde n = 0, de arriba hacia abajo.
# Los valores de cada fila se enumeran desde k = 0 (de izquierda a derecha).
# Los valores que se encuentran en los bordes del triángulo son 1.
# Cualquier otro valor se calcula sumando los dos valores contiguos de la fila de arriba.

# a
# Escribir una función recursiva pascal(n, k) que calcule el número correspondiente. Tener en cuenta que:
#. pascal(n, 0) = pascal(n, n) = 1 si n >= 0
#. pascal(n, k) = pascal(n - 1, k) + pascal(n - 1, k - 1) si n > k > 0.

def pascal(n,k):
    if k == 0 or n == k:
        return 1
    return pascal(n-1, k) + pascal(n-1 , k-1)

# b
# Dibujar el árbol de recursividad para alguna llamada de interés.

def dibujar_pascal(k):
    for i in range(k):
        for j in range(i+1):
            print(pascal(i,j), end=" ")
        print()
 

#%%
# 12. ★★☆ Escribir una especificación apropiada para la siguiente función. Se asume que n es un número
# entero:
def f(n):
    '''devuelve el numero espajado o dado vuelta. ej 1234 -> 4321'''
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))

# %%

# 13. ★★☆ Dadas las siguientes funciones:
# ¿Qué retorna g(2112)? retorna 6
# Escriba una especificación para la función h()

def g(x):
    return h(str(x))

def h(xs):
    '''devuelve la suma de los digitos de un numero'''
    if len(xs) == 1:
        return int(xs)
    n = int(xs[0]) + int(xs[1])
    if len(xs) == 2:
        return n
    else:
        return n + h(xs[2:])



# %%

# 14- Tenemos una tupla de tuplas donde, para cada tupla, se cumple siempre lo siguiente:

# La tupla tiene 3 elementos.
# El primer elemento de la tupla (izquierda) es None o una tupla como las que aquí se describen.
# El segundo elemento (centro) es un número.
# El tercer elemento de la tupla (derecha) es None o una tupla como las que aquí se describen.
# Todos los números que se encuentren en (izquierda) o alguna de las tuplas que contenga (izquierda) son menores a (centro).
# Todos los números que se encuentren en (derecha) o alguna de las tuplas que contenga (derecha) son mayores a (centro).
# Por ejemplo, la siguiente tupla cumple lo mencionado:

# (((None, 4.2, None), 9.8, None), 17.5, ((None, 21.32, None), 28, (None, 32.7, None)))
# Esto lo podemos dibujar como:

#                                           (  , 17.5,  )
#                                            /         \
#                             (  , 9.8, None)          (  , 28,  )
#                              /                        /       \
#             (None, 4.2, None)       (None, 21.32, None)       (None, 32.7, None)


# Escribir una función recursiva que, mediante la estrategia de división y conquista, dada una variable con la tupla de tuplas y un número devuelva si el número está presente en la tupla de tuplas o no.
# Dar ejemplos de ejecución del código declarando las variables y funciones utilizadas.


def is_in_tuple(tupla, n):
    if tupla[1] == n:
        return True
    
    if n < tupla[1]:
        return is_in_tuple(tupla[0], n)
    else:
        return is_in_tuple(tupla[2], n)


