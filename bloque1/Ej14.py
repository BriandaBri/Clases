
def dia(n):
    e = 'La semana tiene 7 dias, imbecil'
    sem = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    if n > 0 and n < 8:
        return sem[n - 1]
    else:
        return e

n = 0

print dia(n)