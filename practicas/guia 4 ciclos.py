# %%
import random
from unittest import result

'''Escribir un programa que pida al usuario cuatro números A, B, C, y D e imprima en la pantalla
todos los números múltiplos de, a la vez, C y D, en el intervalo [A, B).'''


def multiplos_de_c_d(a,b,c,d):
    result = []
    c_mult = [c*n for n in range(1,b) if a < c*n < b]
    d_mult = [d*n for n in range(1,b) if a < d*n < b]

    return set(c_mult).intersection(d_mult)


def basic_multiplication(a,b):
    result = 0
    for i in range(0,b):
        result +=a
    return result


def gauss(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result

def factorial_a(n):
    result = 1
    if n == 0:
        return 1

    for i in range(1,n+1):
        result *= i
    return result 


def numero_combinatorio(n,k):
    return factorial_a(n)/factorial_a(k)*factorial_a(n-k)


def exponential_aprox(x):
    N = 100
    result = 0
    for i in range(0,N):
        result += x**i/factorial_a(i)
    return result

def greatest_odd(n:list):
    result = 0
    for i in n:
        if i > result and i % 2 !=0:
            result = i

    return result

def prime_number_interval(N):
    result = []
    test_p = 1
    flag = False
    while test_p < N:
        flag = False
        test_p +=1
        for i in range(2,test_p):
            if test_p%i == 0:
                flag = True
        if not flag: 
            result.append(test_p)

    return result

def is_prime_number_0_100(n:int):
    flag = False
    if n%1 == 0 and 0 < n < 100:
        for i in range(2, n):
            if (n % i) == 0:
                flag = True
                break
        if flag:
            print(n, "is not a prime number")
        else:
            print(n, "is a prime number")
    else:
        print(n, 'is not an intiger number between 0 and 100')


def equispaciados(start, end,step):
    espacio = (end - start)/(step-1)
    result = [start]
    for i in range(step-2):
        result.append(start+ espacio*(i+1))
    result.append(end)
    return result



def tabla_f_to_c():
    # (F − 32) × 5/9
    valores = input('input the start, end and step separated by spaces ei. 0 100 11').split()
    tabla_f = equispaciados(float(valores[0]),float(valores[1]),int(valores[2]))
    tabla_c = equispaciados((float(valores[0])-32)*(5/9),(float(valores[1])-32)*(5/9),int(valores[2]))
    
    for i in range(int(valores[2])):
        print(f'''| f: {tabla_f[i]} | c: {round(tabla_c[i], 2)} |''')

# to do
def fibonacci(N):
    lista = [0,1]
    result = []
    for i in range(N):
        lista.append(lista[i] + lista[i+1])
        result.append(lista[i]+lista[i+1])
    return result

# to do
def raiz_cubica(K):
    pass


# preguntar cuando tendria que imprimir q no existe, si root es libre y 3234 ** 1 es 3234
def raro(K):
    '''Escriba una función que le pida al usuario ingresar un número y que devuelva dos enteros, root
y pwr, tal que 0 < pwr < 6 y root ** pwr sea igual al número ingresado. Si los dos enteros no
existen, que imprima un mensaje de aviso.'''
    root = 0
    pwr = 1
    while root <= K:
        for pwr_test in range(1,6):
            print(root,pwr_test)
            if root**pwr_test == K:
                return root, pwr_test
        root += 1

def rock_paper_scissors():
    while True:
        player = input('type r p s :')
        computer = random.choice(['r','s','p'])
        print(f'you chose: {player} and the computer chose: {computer}')
        if player == 'r' and computer == 's' or player == 'p' and computer == 'r' or  player == 's' and computer == 'p':
            print('you win')
        elif player == 's' and computer == 'r' or player == 'r' and computer == 'p' or  player == 'p' and computer == 's':
            print('computer wins') 
        else:
            print("it's a tie")
       
        print('\n next round... \n')

def dados():

    while True:
        player1 = 0
        player2 = 0

        while True:
            input('input anything to throw the dice player1 > ')
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            print(f'dados player1 {d1} , {d2}')
            player1 += d1 + d2

            if d1 != d2:
                break

        
        print(f'\n puntaje jugador 1: {player1}')

        while True:
                input('input anything to throw the dice player2 > ')
                d1 = random.randint(1,6)
                d2 = random.randint(1,6)
                print(f'dados player2 {d1} , {d2}')
                player2 += d1 + d2

                if d1 != d2:
                    break


        print(f'\n puntaje jugador 2: {player2}')



# %%

