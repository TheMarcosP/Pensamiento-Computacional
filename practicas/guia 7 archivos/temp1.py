# -*- coding: utf-8 -*-
#%%

def millenials(lista):
    result = []
    for nombre, nacimiento in lista:
        if 1981 <= int(nacimiento.split('/')[2]) <= 1995:
            result.append(nombre)
    return result
# %%
while True:
    try:
        numero = int(input('n > '))
    except ValueError:
        continue
    else:
        print('hola')

# %% 

numeros = []
n = float(input('c > '))
while n != 'esc':
    numeros.append(n)
    n = float(input('number to enter more, "esc" to end > '))
    print(sum(numeros)/len(numeros))

# %%

def find_outlier(n):
    if (n[0]%2==0 and n[1]%2==0) or (n[1]%2==0 and n[2]%2==0) or (n[0]%2==0 and n[2]%2==0):
        for i in n: # pares
            if i%2 != 0:
                return i
    else:
        for i in n: # impares
            if i%2 == 0:
                return i

import string

string.ascii_lowercase

# %%

import string

def high(x):
    result = ''
    temp1 = 0
    value = string.ascii_lowercase
    for word in x.split():
        print(word)
        temp2 = 0
        for letter in word:
            temp2 += 1 + value.index(letter)
            print(temp2, temp1)
        if temp2 > temp1:
            temp1 = temp2
    return x.split()[temp1 + 1]

# %%

def valid_parentheses(x:str):
    only_parentesis = ''
    for i in x:
        if i == ")":
            only_parentesis += ')'
        elif i == "(":
            only_parentesis += '('
    return only_parentesis

# %%

def tribonacci(signature, n):
    if n-3 > 0:
        for i in range(n-3):
            signature.append(signature[i] + signature[i+1] + signature[i+2])
        return signature
    else:
        return signature[0:n]
    
# %%

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    result = []
    for i in range(a,b+1):
        print('i',i)
        result_temp = 0
        for j,num in enumerate(list(str(i))):
            result_temp += int(num)**(int(j)+1)

        if result_temp == i:
            result.append(result_temp)
    return result

# %% solucion pro

def filter_func(a):
    return sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a

def sum_dig_pow(a, b):
    return filter(filter_func, range(a, b+1))

# %% solucion pro

def camel_case(string):
    '''
    "camel case" -> "CamelCase"
    '''
    return string.title().replace(" ", "")

# %%

def busqueda_binaria(lista,target):
    lista.sort()
    izq = 0
    der = len(lista) -1
    while izq<der:
        print(izq<der)
        medio = (izq+der)//2
        print('izq:',izq,'der:',der,'medio',medio)
        if lista[medio] == target:
            return medio
        elif lista[medio] > target:
            der = medio-1
        else:
            izq = medio+1
    return -1
    

# %%




def comp(array1, array2):
    flag = False
    if not (array1 == [] or array2==[]):
        for element in array1:
            if element**2 not in array2:
                flag = True
            else:
                array2.pop(array2.index(element**2))
            if flag:
                return False
        return True
    elif (array1 == [] and array2 == []):
        return True
    else:
        return False

# %%

def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False
    
#%%
cadena = "19 23 1988"
print("/".join(cadena))
