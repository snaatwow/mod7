def divisors(a):
    res = []
    for i in range(1, a + 1):
        if a % i == 0:
            res.append(i)

    return res


print(divisors(180000))