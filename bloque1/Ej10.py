def per(r):
    p = 2 * 3.1416 * r
    return p


def ar(r):
    a = 3.1416 * r**(2)
    return a


def main(r):
    print per(r), ar(r)

print 'Radio: '
r = input()

main(r)