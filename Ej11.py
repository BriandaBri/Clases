

def sal_bruto(h, ph):
    if h > 40:
        bruto = ph * (40 + (1.5 * (h - 40)))
    else:
        bruto = ph * h
    return bruto

print 'Numero horas: '
a = input()

print 'Precio por hora: '
b = input()


print sal_bruto(a, b)