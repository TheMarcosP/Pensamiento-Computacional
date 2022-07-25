# %%
import math 


def Tabla_bool(a,b,c):
    if (a == True and c!= True) or all([a,b,c]): 
        return True
    return False

def resolvente(a,b,c):
    if (b**2)-4*a*c > 0:
        x1 = (-b+math.sqrt((b**2)-4*a*c))/(2*a)
        x2 = (-b-math.sqrt((b**2)-4*a*c))/(2*a)
        if x1 == x2:
            return [x1]
        else:
            return [x2,x1]


def que_dia(n:int):
    # el año comoienza dia lunes
    lista = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
    return lista[n%7]

def que_dia_enchanced(n:int,dia_de_comienzo: str):
    lista = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
    return lista[(n%7)+lista.index(dia_de_comienzo)]   


def x_interseccion(m1,b1,m2,b2):
    if m1-m2 == 0:
        if b1 == b2:
            print('las rectas compatibles indeterminadas')
            return None
        else:
            print('las rectas no tienen interseccion')
            return None
    else:
        return (b2-b1)/(m1-m2)


#%%
# ejercicio 10

def is_bisiesto(n):
    if n%4 == 0 and (n%100 != 0 or n%400 == 0):
        return True
    return False

def dias_del_mes(month,year):

    diccionario = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31,
    }
    if is_bisiesto(year) and month == 2:
        return 29
    
    else:
        return diccionario[month]

def is_date_valid(day,month,year):

    if 0 < month < 13 and (0 < day <= dias_del_mes(month,year)):
        return True
    else:
        return False
    
def dias_hasta_fin_de_mes(day,month,year):

    if is_date_valid(day,month,year):
        return dias_del_mes(month,year) - day


def dias_hasta_fin_de_year(day, month, year):
    result = 365
    
    if is_date_valid(day,month,year):
        for i in range(1, month):
            result -= dias_del_mes(i, year)
        result -= day
        return result
      

def dias_transcurridos(day,month,year):
    return 365 - dias_hasta_fin_de_year(day,month,year)


def diferencia_entre_fechas(day1, month1, year1, day2, month2, year2):
    return abs(abs(dias_transcurridos(day1, month1, year1) - dias_transcurridos(day2,month2,year2)) - abs(365*(year1 - year2)))


def dias_hasta_primavera(day,month,year):
    if month <= 9:
        return diferencia_entre_fechas(day,month,year,21,9,year)
    else:
        return diferencia_entre_fechas(day,month,year,21,9,year+1)



# ej 15

def ganancia_tna(tna,capital,fecha_in,fecha_out):

    
    dias = diferencia_entre_fechas(fecha_in[0],fecha_in[1],fecha_in[2],fecha_out[0],fecha_out[1],fecha_out[2])
    if dias >= 30:
        return capital + capital*(tna/(100*365))*dias

def ganancia_tna_dias(tna, capital, dias):
    if dias >= 30:
        return capital + capital*(tna/(100*365))*dias

def dias_hasta_retorno(tna,capital,capital_esperado):
    return (capital_esperado-capital)/(capital*(tna/(100*365)))

def capital_para_retorno(tna,capital_esperado,tiempo):
    return capital_esperado/(1 + (tna/(100*365))*tiempo)


def tor_or_xfg(capital,tiempo):
    if capital > 10000000:
        inversion_tor = ganancia_tna_dias(39.5,capital,tiempo)
    else:
        inversion_tor = ganancia_tna_dias(42.5,capital,tiempo)
    
    capital_xfg = capital/200
    xfg = ganancia_tna_dias(0.5,capital_xfg, tiempo )
    inversion_xfg = xfg*(200*((1+0.045/100)**tiempo))
    
    print(f'tor: {inversion_tor}, inversion xfg: {inversion_xfg}')
    if inversion_tor > inversion_xfg:
        return 'Hacer deposito en tor'
    else:
        return 'Convertir a XFG, y hacer el depósito, y convertir el monto final a XFG.'
# %%

