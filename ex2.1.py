from perm import *


def composition(a, b):
    res = []
    for i in range(0, len(a), 1):
        res.append(b[a[i]])

    return res


def inverse(a):
    return list(reversed(a))


def power(a, power):
    res = a
    if power >= 0:
        for i in range(0, power - 1, 1):
            res = composition(res, a)

    else:
        for i in range(0, power + 1, -1):
            res = composition(res, inverse(a))

    return res


def period(p):
    i = 1
    while True:
        if is_trivial(power(p, i)):
            break

        i+= 1

    return i



#p = [1, 2, 3, 0, 5, 6, 4, 8, 7]
#print_permutation(p)
#q = composition(p, p)
#p2 = power(p, 2)
#print_permutation(p)
#print(q)
#print_permutation(p2)
#print(period(p))
#print_permutation(p)
# print(inverse(cycles(q)))

#p = test_permutation(100)
p = [0, 2, 1, 3, 4]
q = composition(p, p)
print_permutation(q)
print(period(p))