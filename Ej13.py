
def voc(l):
    vocal = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    if l in vocal:
        return True
    else:
        return False
l = 'a'

print voc(l)