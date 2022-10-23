def rom_thous(x):
    xth = x // 1000
    if xth == 2:
        rth = ['MM']
    else:
        rth = ['M']
    return rth

def to1_9(x : int, y : list, c : list, z : list): # y = d c = c z = m
    r = ['']
    if x == 9:
        r.append(c + z)
    if 6 <= x <= 8:
        r = [y]
        i = 6
        while i <= x:
            r.append(c)
            i = i + 1
    if x == 5:
        r = [y]
    if x == 4:
        r.append(c + y)
    if 1 <= x <= 3:
        r = ['']
        i = 1
        while i <= x:
            r.append(c)
            i = i + 1
    return r


x= int(input("x = "))

if x >= 1000:
    x1 = x % 1000
    xh = x1 // 100
    xt1 = x1 % 100
    xt = xt1 // 10
    xo = xt1 % 10

    r = rom_thous(x) + to1_9(xh, 'D', 'C', 'M') + to1_9(xt, 'L', 'X', 'C') + to1_9(xo, 'V', 'I', 'X')

if 100 <= x < 1000:
    xh = x // 100
    xt1 = x % 100
    xt = xt1 // 10
    xo = xt1 % 10
    r = to1_9(xh, 'D', 'C', 'M') + to1_9(xt, 'L', 'X', 'C') + to1_9(xo, 'V', 'I', 'X')

if x < 100:
    xt = x // 10
    xo = x % 10
    r = to1_9(xt, 'L', 'X', 'C') + to1_9(xo, 'V', 'I', 'X')

print(''.join(r))

