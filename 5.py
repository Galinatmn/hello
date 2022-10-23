def getTen(y):
    t: int = 0
    for b in y:
        b = int(b)
        t = t + b + t
    return t

def multipl(x1, x2):
    t1 = getTen(x1)
    t2 = getTen(x2)
    t = t1 * t2
    return t

def getBin(x1, x2):
    x = multipl(x1, x2)
    b = ''
    while x > 0:
        b = str(x % 2) + b
        x = x // 2
    return (b)


x1 = input('Ввод: x1 = ')
x2 = input('Ввод: x2 = ')

getTen(x1)
getTen(x2)
multipl(x1, x2)
print('Вывод: ' + getBin(x1, x2))
print(f'Пояснение: “{x1}” - это {getTen(x1)}; “{x2}” - это {getTen(x2)}; {getTen(x1)}*{getTen(x2)} = {multipl(x1, x2)};'
      f' {multipl(x1, x2)} в двоичной системе {getBin(x1, x2)}.')