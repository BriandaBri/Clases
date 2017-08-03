
em = []

def micro_empresa(em):

    p = [50, 30000000, 5000000]
    cont = 0
    for i in em:
        if i < p[cont]:
            cont += 1
        else:
            return False
    return True

pres = [1, 1, 1]

print micro_empresa(pres)
