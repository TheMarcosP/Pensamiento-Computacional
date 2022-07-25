# %%

import string


def count_A(the_string: str) -> int:
    counter = 0
    for i in the_string:
        if i.lower() == 'a':
            counter += 1
    return counter


def count_letter_in_string() -> int:
    string = input('ingrese el str : ')
    letra = input('la letra a contar: ')
    counter = 0
    for i in string:
        if i.lower() == letra:
            counter += 1
    return counter


# forma lenta
def ip_con_colmillos(ip: str) -> str:
    iplist = ip.split('.')
    colmillos = ''
    for i in iplist:
        colmillos += i + '[.]'
    return colmillos


# forma rapida


def ip_con_colmillos_bien(ip: str) -> str:
    ip = ip.replace('.', '[.]')
    return ip


def contar_joyas(conjunto: str, joyas: str) -> int:
    counter_de_joyas = 0
    for i in conjunto:
        if i in joyas:
            counter_de_joyas += 1
    return counter_de_joyas



def acortador(mensaje: str, n: int) -> int:
    cantidad = len(mensaje) - n
    result = ''

    if n > 3:
        if cantidad > 0:
            for i in range(0,cantidad):
                result += mensaje[i]
            result += '.'*n
        return result
    elif 0 < n < 4:
        return '.'*n
    
    elif n < 0:
        return ''

def acortador_v2(mensaje: str, n: int) -> int:
    pass
    

def is_safe(password):
    lower, upper, number, signo, lenght = False, False, False, False, False
    for i in password:
        if i in string.ascii_lowercase:
            lower = True
            print('lower')
        if i in string.ascii_uppercase:
            upper = True
            print('upper')
        if i in '0123456789':
            print('int')
            number = True
        if i in string.punctuation:
            print('signo')
            signo = True
    if 8 < len(password) < 31:
        print('len')
        lenght = True
    if all([lower, upper, number, signo, lenght]):
        return True
    else:
        return False


def is_sagitarian(date: str) -> bool:  # date as AAAA-MM-DD
    if (date.split('-')[1] == '11' and 22 <= int(date.split('-')[2]) <= 31) or ((date.split('-')[1]=='12' and 1 < int(date.split('-')[2]) <= 21)):
        return True
    return False


def cesar_coder(msg: str, n: int) -> str:
    result = ''
    for i in msg:
        result += chr(ord(i)+n)
    return result


def cesar_decoder(msg: str, n: int) -> str:
    result = ''
    for i in msg:
        result += chr(ord(i)-n)
    return result


def matches(base: str, word: str) -> bool:
    if len(base) != len(word):
        return False
    for i, letter in enumerate(base):
        if letter == "?":
            pass
        else:
            if letter == word[i]:
                pass
            else:
                return False
    return True


def test_matches():
    if matches("?", ""):
        return False
    if not matches("?", "a"):
        return False
    if matches("?", "aa"):
        return False
    if matches("x", "a"):
        return False
    if not matches("?o?a", "rota"):
        return False
    if not matches("?o?a", "poca"):
        return False
    if not matches("?o?a", "bota"):
        return False
    if not matches("?o?a", "sola"):
        return False
    if not matches("?o?a", "cosa"):
        return False
    if matches("?osa", "rota"):
        return False
    if matches("?ola", "poca"):
        return False
    if matches("co?a", "bota"):
        return False
    if matches("mo?a", "sola"):
        return False
    if matches("so?a", "cosa"):
        return False
    else:
        return True


def terminan_en_vocal(lista:list):
    result = []
    for lis in lista:
        if lis[-1] in 'aeiouAEIOU':
            result.append(lis)
    return result

def distribucion_de_longitud_de_palabras(parrafo:str):
    distribucion = {}
    
    lista_de_palabras = parrafo.split()
    
    for i, palabra in enumerate(lista_de_palabras):
        new_string = ''.join(char for char in palabra if char.isalnum())
        lista_de_palabras[i] = new_string

    for i,palabra in enumerate(lista_de_palabras):
        largo = len(palabra)
        if f'palabras de largo {largo}' in distribucion.keys():
            distribucion[f'palabras de largo {largo}'] +=1
        else:
            distribucion[f'palabras de largo {largo}'] = 1
    
    return distribucion

def delete_last_element(lista:list, n: int) -> list:  # [[0,1,3],[4,6,3],[2,6,1]]
    for sublist in lista:
        if sublist[-1] > n:
            sublist.pop()
    return lista

def sum_of_elements(lista:list) -> bool:
    count = 0
    for i in lista:
        count += i
    if count == 9:
        return True
    else:
        return False


def filtrar(lista: list, function):
    result = []
    for sublista in lista:
        if function(sublista):
            result.append(sublista)
    return result


# %%
