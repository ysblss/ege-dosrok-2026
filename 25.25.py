
def f(n):
    a = []
    for d in range(2, int(n**0.5)+ 1):
        if n % d == 0:
            d1 = d
            if d1 % 10 == 7 and d1 != 7:
                a.append(d1)
            d2 = n // d
            if d2 % 10 == 7 and d2 != 7:
                a.append(d2)

    return a
c = 0
for i in range(700000, 1000000):
    r = f(i)
    if len(r) > 0:
        print(i, min(r))
        c+=1
    if c == 5:
        break
