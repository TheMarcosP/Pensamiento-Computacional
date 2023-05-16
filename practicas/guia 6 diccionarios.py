# %%
# 4. ★☆☆ Escriba una función que recibe un número y devuelve un diccionario cuyas claves son desde el
# número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

import imp
from random import random


def dic_num(n):
    dic = {}
    for i in range(1,n+1):
        dic[i] = i**2
    return dic
a = dic_num(5)
# %%

# 5. ★☆☆ Escriba una función que recibe una cadena y devuelve un diccionario con la cantidad de
# apariciones de cada carácter en la cadena.

def count_dic(cadena):
    dic = {}
    for letter in cadena:
        if letter in dic.keys():
            dic[letter] +=1
        else:
            dic[letter] = 1
    return dic

#%%
# 8. ★★★ Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde las
# claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos. Por ejemplo

def lista_de_tuplas_a_diccionario(lista):
    dic = {}
    for tupla in lista:
        list(tupla)
        if tupla[0] in dic.keys():
            dic[tupla[0]] = list((dic[tupla[0]], tupla[1]))
        else:
            dic[tupla[0]] = tupla[1]
    return dic

l  = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'),('Buenos', 'días') ]

print(lista_de_tuplas_a_diccionario(l))       
# %%
# 9. ★★☆ Escribir una función que reciba la cantidad de iteraciones a realizar de una tirada de 2 dados y
# devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados.

import random

def frecuencia_de_tiradas(n):
    dic = {}
    for tirada in range(n):
        suma_dados = str(random.randint(1,6) + random.randint(1,6))
        if suma_dados in dic.keys():
            dic[suma_dados] += 1
        else:
            dic[suma_dados] = 1
    return dic

# %%

# 10. ★★☆ Implementamos una agenda con un diccionario, donde almacenamos nombres y números
# telefónicos. Escribir un programa que vaya solicitando al usuario que ingrese nombres, luego:
# 1. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir
# modificarlo si no es correcto.
# 2. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
# El usuario puede utilizar la cadena ”*”, para salir del programa.

def contacts_menu():
    dic = {}
    while True:
        name = input('enter the name of your contact: ')
        print(dic.keys(), name)
        if name == '*':
            print('end')
            break
        print(name,dic.keys(),name in dic.keys())
        if name in dic.keys():
            print('entro')
            change_num = input(f'the phone number of {name} is: {dic[name]}. Is it correct? [y/n]:')
            if change_num == 'n':
                dic[name] = input('enter the correct phone number: ')
                print('Saved!')
        else:
            dic[name] = input('enter the phone number of your contact: ')
            print('saved!')
    print(dic)

# %%

# 11. ★★★ Escribir un archivo llamado words.py que contenga una variable que sea una lista con palabras
# (strings). Escribir, luego, una función que lea las palabras en words.py y las almacene como valores en
# un diccionario. La clave a la que pertenece cada palabra es su propia longitud. Luego se pueden
# recuperar rápidamente todas las palabras de una determinada longitud.
from words import words
def lenght_split(lista):
    dic = {}
    for word in lista:
        if len(word) in dic.keys():
            dic[len(word)] += [word]
        else:
            dic[len(word)] = [word]
    return dic

# %%
# 12. ★★★ Lea que es un bit de paridad [https://en.wikipedia.org/wiki/Parity_bit] y cree una función que
# reciba una lista de strings con 7 bits y devuelva un diccionario donde estos strings sean las claves y el
# parity bit el valor.

def bit(lista):
    dic = {}
    for cadena in lista:
        if cadena.count('1')%2 == 0:
            dic[cadena] = 0
        else:
            dic[cadena] = 1
    return dic


# %%
# 13. ★★★ Lea que es un Cyclic redundancy check [https://en.wikipedia.org/wiki/Cyclic_redundancy_check] y
# cree una función que reciba una lista de strings con 7 bits y devuelva un diccionario donde estos strings
# sean las claves y el CRC (de 4 bits de largo) el valor asociado



## clase 1 flor

dictionario = {'a':1,'b':2,'c':3,'d':4,'e':5}

dictionario["d"]

dictionario.keys()


# %%

# a. Escribir una función que reciba una estación y devuelva las líneas que pasan por esa estación. b. Escribir una función que pida al usuario una estación de origen y otra de destino e indique qué línea tomar para ir de una a otra. Si no hay conexión directa, debe indicar cuáles son las estaciones de conexión.

# En una realidad alternativa la red de subterráneos de Buenos Aires está compuesta por 4 líneas, A, C, D y E. Cada línea tiene 3 estaciones, y nunca hace falta hacer más de un cambio de línea para ir de una estación a otra. Los siguientes diccionarios describen la red:

subtes = {"A", "C", "D", "E"}
estaciones = {"A": ["Acoyte", "Avenida de Mayo", "Callao"],
          "C": ["Avenida de Mayo", "Congreso", "Urquiza"],
          "D": ["Pellegrini", "Urquiza", "Callao"],
          "E": ["Pellegrini", "Lima", "Avenida de Mayo"]}


def get_lineas(estaciones, estacion):

    lineas_que_pasan_estacion = []

    for lineas in estaciones.items():
        linea = lineas[0]
        estaciones_de_linea = lineas[1]

        if estacion in estaciones_de_linea:
            lineas_que_pasan_estacion.append(linea)

    return lineas_que_pasan_estacion


get_lineas(estaciones, "Avenida de Mayo") # [A,B,C]

# %%
