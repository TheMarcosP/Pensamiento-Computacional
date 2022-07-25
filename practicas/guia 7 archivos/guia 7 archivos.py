# %%

def cp(file1 : str,file2 : str):
    with open(file1,'r') as f1, open(file2,'w') as f2:
        for line in f1:
            print(line)
            f2.write(line)

cp('t1.txt','t2.txt')

# %%
# ej 6
def wc(file : str):
    lineas =0
    palabras= 0 
    caracteres = 0
    with open(file,'r') as f:
        for line in f:
            lineas += 1
            palabras += len(line.split())
            caracteres += len(line)
    print(lineas,palabras,caracteres, file)
# %%
# ej 7
def grep(archivo : str,cadena : str):
    with open(archivo,'r') as f:
        for line in f:
            if cadena in line:
                print(line)
# %%
# 9. ★★☆ Escribir una función, llamada rot13, que reciba un archivo de texto de origen y uno de
# destino, de modo que para cada línea del archivo origen, se guarde una línea cifrada en el archivo
# destino. El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter comprendido entre la a y
# la z (del alfabeto inglés), se le suma 13 y luego se aplica el módulo 26, para obtener un nuevo
# caracter.
from string import ascii_lowercase

def rot13(file1,file2):
    with open(file1,'r') as f, open(file2,'w') as g:
        for line in f:
            g.write(encrypt(line))


def encrypt(cadena):
    encrypted = ''
    for char in cadena:
        try:
            index = ascii_lowercase.index(char)
        except ValueError:
            encrypted += char
        else:
            encrypted += ascii_lowercase[(index+13)%26]
    return encrypted            
#%% 
# 10
def load_data(file:str):
    dicti = dict()
    with open(file,'r') as f:
        for line in f:
            dicti[line.split(":")[0]] = line.split(':')[1][:-1]
    return dicti

# %%
# 11 mejor forma de hacerlo?

def sed(file,find:str,replace:str):
    new = ''
    with open(file,'r') as f:
        for line in f:
            new += line.replace(find,replace)
    with open(file,'w') as f:
        f.write(new)

#%%
# 15. ★★☆ Dado el siguiente archivo de texto, que contiene un guion de la serie Seinfeld:
# 1. Eliminar los nombres de los personajes.
# 2. Eliminar lineas en blanco.
# 3. Eliminar puntuaciones.
# 4. Eliminar informacion adicional para los actores.
# 5. Guardar el archivo con los cambios.

def clean_text(file):
    with open(file,'r') as f:
        text = ''
        for line in f:
            # borro lineas en blanco
            if not line.isspace():
                # borro el nombre del actor
                try:
                    start = line.index(':') + 1
                except ValueError:
                    start = 0

                text += line[start:]
        
        clean = ''
        # borro lo que esta en parentesis
        in_parenthesis = False
        for char in text:
            if char == '(':
                in_parenthesis = True

            if char not in ',.?!' and not in_parenthesis:
                clean += char
                
            elif char == ')':
                in_parenthesis = False

        return clean

def overwrite_file(file,text):
    with open(file,'w') as f:
        f.write(text)


# %%
# ej 16
import math

def csv_to_list(file,file2):
    with open(file,'r') as f, open(file2,'r') as f2:
        lista = []
        for line in f:
            lista.append(line.split(',')[0:2])
        for line in f2:
            for l in lista:
                if l[0] == line.split(',')[0]:
                    l.extend(line.split(',')[1:])
        
        return list(lista[1:])

def calc_speed(dino):
    stride_length =float(dino[1]) 
    leg_length = float(dino[2])
    g = 9.8 # gravity constant
    return ((stride_length / leg_length) - 1) * math.sqrt(leg_length * g)

def order_by_speed(lista):
    x = []
    for i in lista:
        if len(i) == 4 and 'bipedal' in i[3]:
            x.append(i)
    return sorted(x , key = calc_speed)


# %%
# 17. ★★★ Dado un archivo en formato CSV, que contiene canciones (nombre, duración, artista), escribir
# un programa que lea el archivo e imprima por pantalla la lista con el siguiente formato:
"tabla.png"

def csv_to_list(file):
    lista = []
    with open(file,'r') as f:
        for line in f:
            lista.append(line[:-2].split(','))
    return lista


# se podria parametrizar para que se ajuste a distintos largos de strings y mas columnas
def render_table(lista):
    columns = len(lista[0])
    # title
    print('+'+'-'+'-'*30+'+'+'-'*6+'+'+'-'*15+'-'+'+')
    print(f'''| {lista[0][0]:<30}|{lista[0][1]:^6}|{lista[0][2]:<15} |''')
    print('+'+'-'+'-'*30+'+'+'-'*6+'+'+'-'*15+'-'+'+')

    # rows
    for row in lista[1:]:
        print(f'''| {row[0]:<30}|{row[1]:^6}|{row[2]:<15} |''')
    print('+'+'-'+'-'*30+'+'+'-'*6+'+'+'-'*15+'-'+'+')
# %%
# 18. ★★★ Un archivo en formato JSON, es un archivo de texto, pero que su contenido está escrito del
# siguiente modo:

# {
#  "id": 22264,
#  "name": "Jack",
#  "last_name": "Hunt",
#  "age": 38,
#  "children": false,
#  "siblings": "Jessica Hunt, Robin Hunt",
#  "ssn": "1234-99-0012"
# }

# Tiene el mismo formato que un diccionario de Python, pero esta escrito en un archivo de texto.
# Escribir una función que lea el archivo en formato JSON, y transforme el contenido a un diccionario
# de Python. Imprimir el diccionario por pantalla.

import json

def load_dic_from_json(file):
    with open(file,'r') as f:
        return json.load(f)

# %%


# %%
