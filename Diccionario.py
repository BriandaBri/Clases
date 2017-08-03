
lista = []
dic = {}
cont = 0
while cont < 6:

    dic[cont] = {'Paca', cont + 20, cont}
    lista.append(dic)
    cont += 1

print lista

a = open("C:/Users/brian/desktop/Rrrr.txt", "w")
a.write('%s \n' % lista)

a.close()
