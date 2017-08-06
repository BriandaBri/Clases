li = []


def impuesto(li):
    inn = ((li[0] - 600) - 60*li[1])/3
    return inn

g = [1, 1]

print impuesto(g)

