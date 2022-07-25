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

def multi_recursiva(z,k):
    if z != 0:
        return multi_recursiva(z-1,k) + k
    else:
        return 0

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
    if n == '':
        return 0
    return len_digits(str(n)[:-1]) + 1

# %%
#3. ★☆☆ Implementar una función recursiva que reciba un entero no negativo e retorne dicho número
# espejado, es decir, para el 1234 retorna 4321.
import time

from numpy import append

def espejado(numero : int):
    pass
# %%

#%%
# 4. ★☆☆ Escribir una función recursiva que calcule el n-ésimo número triangular (el número triangular de
# n es 1 + 2 + 3 + ··· + n)

def num_triangular(n):
    print(n)
    if n == 1:
        return 1
    return num_triangular(n-1) + n
# %%

# %%

# 5. ★★☆ Implementar una función recursiva que dados dos números n y b retorne True si n es potencia
# de b.

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

def max_vector(vector:list):
    if len(vector) == 1:
        return vector[0]
    if vector[0] > vector[1]:
        vector.pop(1)
    else:
        vector.pop(0)
    return max_vector(vector)
# %%

# 7. ★★☆ Escribir una función recursiva que calcule el n-ésimo número de la sucesión de Fibonacci. La
# misma se define como F_n = F_{n-1} + F_{n-2}, F_0 = F_1 = 1.
# Dibuje un esquema (árbol de recursividad) de las llamadas recursivas para n = 6.

def recursive_fibonacci(n):
    if n <= 1:
        return 1
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

# %%

def gcd(m,n):
    if m == n:
        return m
    if m>n:
        return gcd(m-n,n)
    else:
        return gcd(m,n-m)
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
        return max(max_n(n[:sep]), max_n(n[sep:]))

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
