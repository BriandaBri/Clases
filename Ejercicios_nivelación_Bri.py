
# coding: utf-8

# ## EJERCICIO 1

# Crear una lista de diccionarios que contendran este formato {nombre:"nombre_user", edad:edad_user, codigo_usuario:"codigo_usuario"}
# Volcar la lista sobre un fichero txt

# In[11]:

lista_users = []

for i in xrange(10):
    dict={"nombre":"user_{}".format(i),"edad":10+i,"codigo_usuario":"user_code_{}".format(i)}
    lista_users.append(dict)
    
print lista_users


# In[12]:

with open("users_test.txt","w") as f:
    
    for user in lista_users:
        f.write(str(user))
        f.write("\n")


# ### BLOQUE 1

# #### 1. Función que retorne el mayor de dos números o 0 si son iguales

# In[15]:

def compare(num1,num2):
    
    lista = [num1,num2]
    if num1 == num2:
        return 0
    else:
        return max(lista)


# #### 2. Función que determine si una persona es mayor de edad o no:
# 

# In[39]:

def mayor_edad(edad):
    
    if edad >= 18:
        return True
    else:
        return False


# #### 3. Programar una función que determine si una empresa es microempresa o no (retorno booleano –True o False–). Se dice que es microempresa si tiene menos de 50 empleados, factura menos de 30 milones de euros y tiene un balance igual o inferior a los 5 millones de euros.

# In[43]:

def company_size(n_emp,facturacion,balance):
    
    if n_emp>=50 and facturacion < 30000000 and balance <= 5000000:
        return True
    else:
        return False


# #### 4.Calcular el impuesto que debe pagar un contribuyente a partir de sus ingresos anuales y el número de hijos. El impuesto a pagar es un tercio del ingreso imponible, siendo este último igual a los ingresos totales menos una deducción personal de 600€ y otra deducción de 60€ por hijo.

# In[44]:

def impuesto(ingresos,n_hijos):
    
    impuesto = ((ingresos - 600) - (60 * n_hijos))/3
    return impuesto


# #### 5.Hacer los cálculos que permiten saber si una empresa de 20 empleados, 18 millones de euros de facturación y 5 millones de euros de balance es una micro empresa y almacenar el valor en una variable lógica (booleana).

# In[45]:

es_micro = company_size(20,18000000,5000000)
print es_micro


# #### 6.La temperatura expresada en grados centígrados TC, se puede convertir a grados Fahrenheit (TF) mediante la siguiente fórmula: TF = 9*TC/5 + 32. Programa una función para hacer esta transformación que reciba como argumento la temperatura en grados centígrados y retorne su equivalente en Farenheit.

# In[47]:

def grades_to_TF(TC):
    
    grados_TF = 9 * TC/5 + 32
    return grados_TF


# #### 7.Escribir una función Python que a partir de una cierta cantidad en euros y del tipo de cambio del día, retorne el equivalente en libras teniendo en cuenta que la casa de cambio retiene una comisión del 2% sobre el total de la operación.

# In[48]:

def exchange(amount,change_type):
    
    exchange_value = amount * change_type
    final_value = exchange_value - exchange_value*0.02
    
    return final_value


# #### 8.Procedimiento que pinte una línea de asteriscos en pantalla

# In[55]:

def paint():
    print "############################################"


# ##### 9.Programe un módulo en Python que reutilizando la función anterior muestre nuestros datos en pantalla con formato banner tal y como se representa abajo:
# ******************************
# Autor: Lucas Sánchez
# Email: lucassanchez@campusciff.net
# ******************************

# In[56]:

def banner(autor,email):
    
    paint()
    print "Autor: {0} Email: {1}".format(autor,email)
    paint()
    
banner("Angello","angellor.g@hotmail.com")


# ##### 10. Programa modularizado que, utilizando funciones, calcule el perímetro y el área de un círculo cuyo radio es proporcionado por el usuario

# In[64]:

def perimetro(radio):
    
    perimetro = 2 * 3.141516 * radio
    return perimetro
    
def area(radio):
    
    area = 2 * 3.141516 * radio**(2)
    return area

def main_math_functions():
    
    print "Inserte el radio"
    radio = input()
    
    per = perimetro(radio)
    ar = area(radio)
    
    print "Perimetro:{0} \n Area:{1}".format(per,ar)
    
main_math_functions()


# #### 11. Escribamos un programa para solicitar al usuario el numero de horas y el precio por hora con vistas a calcular su salario bruto. Las horas que sobrepasen 40 se considerarán extra y pagadas a 1,5 veces el precio de la hora regular.

# In[68]:

def sueldo():
    
    print "Inserte las horas:"
    horas = input()
    print "Inserte precio por hora"
    precio = input()
    
    if horas > 40:
        residuo = horas - 40
        sueldo = (40 * precio)+((precio*1.5) * residuo) 
    else:
        sueldo = precio * horas
    
    return sueldo


# #### 12. Programar una función que determine si un número es par o impar. La función debe retornar verdadero o falso haciendo uso de valores booleanos.

# In[71]:

def par(num):
    if num%2 == 0:
        return True
    else:
        return False


# #### 13. Programar una función que determine si una letra es vocal o no.

# In[75]:

def es_vocal(vocal):
    
    vocales=["a","e","i","o","u"]1
    
    if vocal in vocales:
        return True
    else:
        return False


# #### 14. Programar un módulo en Python que a partir de un número entero entre 1 y 7 que recibe como argumento muestre en pantalla el día de la semana que corresponda, y un mensaje de error si el número no está entre 1 y 7.

# In[79]:

def dia_semana(dia):
    
    dias = ["L","M","X","J","V","S","D"]
    if dia>0 and dia <8:
        dia = dia - 1
        print dias[dia]
    else:
        print "[ERROR] Numero fuera de rango"
         


# #### 15. Programar una función en Python que a partir de un número entero entre 1 y 7 que recibe como argumento retorne el día de la semana que corresponda, y un mensaje de error si el número no está entre 1 y 7.

# In[81]:

def return_dia_semana(dia):
    
    dias = ["L","M","X","J","V","S","D"]
    try:
        if dia>0 and dia <8:
            dia = dia - 1
            return dias[dia]
    except Exception:
        print "[ERROR] Numero fuera de rango"
       

