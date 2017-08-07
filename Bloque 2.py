from itertools import izip_longest
import random
import numpy
"""1. Modificar una lista de numeros reales que representan las calificaciones de los
alumnos de una clase, para sustituir los valores numericos por sus
calificaciones alfanumericas (Suspenso, Aprobado, etc.)"""


def convert(num):
    if num < 5:
        return 'Suspenso'
    if num == 5:
        return 'Aprobado'
    if num == 6:
        return 'Bien'
    if num == 7 or num == 8:
        return 'Notable'
    if num == 9 or num == 10:
        return 'Sobresaliente'
    else:
        return 'Fuera de rango'

#print convert(5)

"""2. Implementar una funcion que pone en mayusculas todas las primeras letras
de las palabras de una frase."""


def upper(a):
    return a.title()

#print upper('la paca')

"""3. Implemente una funcion que indique si una palabra contiene las cinco
vocales: por ejemplo murcielago. Modifique posteriormente la funcion para
que detecte solo aquellas palabras que contienen una unica vez cada vocal."""


def allvocal(a):

    a = a.lower()
    if 'a' in a and 'e' in a and 'i' in a and 'o' in a and 'u' in a:
        return True
    else:
        return False


def onevocal(a):

    a = a.lower()
    voc = ['a', 'e', 'i', 'o', 'u']
    cont = 0

    for i in a:
        for v in voc:
            if i == v:
                cont += 1

    if cont == 1:
        return True
    else:
        return False

#print onevocal('hhU')

"""4. Escribir una funcion que sume dos listas de igual longitud y retorne otra lista
que contenga la suma de las originales elemento a elemento."""


def sum(a, b):
    if len(a) == len(b):
        li = [x + y for x, y in zip(a, b)]
        return li
    else:
        return 'Desiguales'

#print sum([1, 1], [2, 2])

"""5. Modifique el ejercicio anterior permitiendo que las listas sean desiguales. En
este caso, los elementos sobrantes de la lista mas larga se anadiran al final
de la lista resultante."""


def summ(a, b):
    if len(a) == len(b):
        li = [x + y for x, y in zip(a, b)]
        return li
    else:
        final_list = [x + y for x, y in izip_longest(a, b, fillvalue=0)]
        return final_list

#print summ([1, 4], [1])

"""6. Crear una lista de enteros, inicializarlos segun valores aleatorios en el rango
1..20 y computar la media de los valores, el valor mas alto y el mas bajo todo
ello utilizando listas. Utilizar las funciones para generacion de numeros
aleatorios de Python https://docs.python.org/dev/library/random.html"""

def measure():
    list = [random.randint(0, 20) for r in xrange(10)]
    med = numpy.mean(list)
    max = numpy.max(list)
    min = numpy.min(list)
    return list, med, max, min

#print measure()

#7. Implementar una funcion que compruebe si una palabra es un palindromo.

def palin(a):
    a = list(a)
    b = a[::-1]
    if a != b:
        return False
    return True

#print palin('oaiao')

"""8. Crear una funcion que compruebe si dos cadenas de caracteres son iguales
recorriendo con un indice ambas cadenas (no puede utilizar cad1==cad2)."""


def compare(a, b):
    if id(a) - id(b) == 0:
        return True
    else:
        return False

#print compare('Paca', 'Paca')

"""9. Distribuir 20 datos enteros leidos por teclado en dos listas de tal manera que
se vayan generando dos secuencias ordenadas, una creciente y otra
decreciente."""


def seq():
    cont = 0
    li = []
    il = []
    while cont < 11:
        print 'Numero ', cont, ' :'
        n = input()
        li.append(n)
        li = sorted(li)
        il = li[::-1]
        cont += 1
    return li, il

#print seq()

"""10. Escriba un programa que codifique una frase modificando todas las vocales
segun el siguiente codigo: a por 4, e por 3, i por 1, o por 0 y u por el
simbolo #. Por ejemplo, la frase: Un perro del hortelano, debera
devolverse: #n p3rr0 d3l h0rt3l4n0."""


def codif(a):
    a = a.lower()
    a = [i for i in a]
    for i in xrange(len(a)):
        if a[i] == 'a':
            a[i] = '4'
        if a[i] == 'e':
            a[i] = '3'
        if a[i] == 'i':
            a[i] = '1'
        if a[i] == 'o':
            a[i] = '0'
        if a[i] == 'u':
            a[i] = '#'
    return "".join(a)

#print codif('murcielago')

"""11.Crear un diccionario en python con parejas numero de tfno, nombre que
represente una agenda telefonica. Posteriormente simular un manos libres,
pidiendo al usuario A quien desea llamar y mostrando en pantalla el
mensaje Llamada al numero XXX en curso donde XXX seria el numero
telefonico de la persona elegida."""


def agenda():
    ejemplo = {'Paca': 646589332, 'Aurelio': 654892475, 'El Bryan': 711453668}
    print 'A que usuario desea llamar?'
    n = raw_input()
    if n in ejemplo:
        print 'Llamada al numero ', ejemplo[n]
    else:
        print 'El usuario ', n, ' no esta en tu lista de contactos.'

#agenda()


#12. Escribir una funcion que reciba un tweet y retorne los hashtags en una lista

def twit(a):
    output = []
    for i in a.split(' '):
            if i[0] == '#':
                output.append(i)
    return output

#print twit('Berberechos #en #vinagre')

"""13. Escriba un programa que lea un archivo de texto y lo mete en una lista
donde cada linea es una sublista"""


def leer():
    with open("Texto", "r") as lista:
        texto = lista.readlines()
        return texto

print leer()

"""14.Realizar un programa que lea palabras hasta que se introduzca fin,
mostrando una estadistica de las longitudes de las palabras, es decir, el
numero total de palabras de longitud 1 que se hayan introducido, el total de
longitud 2, etc. La maxima longitud de las palabras debera ser de 25
caracteres. Una posible salida de este programa seria:
Palabras longitud 1: 0
Palabras longitud 2: 10
...
Palabras longitud 25: 1"""


def wordlong():
    li = []
    total = []
    bul = True
    while bul:
        print 'Palabra: '
        n = raw_input()
        if len(n) > 25:
            print '25 letras maximo'
        if n == 'fin':
            bul = False
        else:
            li.append(len(n))

    for i in xrange(26):
        cont = li.count(i)
        total.append(cont)
    cont = 0
    for i in total:
        if total[i] != 0:
            print 'De ', cont, ' letras : ', i
        cont += 1

#print wordlong()
