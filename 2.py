def palindrom(x):
    new_x = x.replace(' ', '')
    reverse_new_x = new_x[::-1]
    reverse_x = x[::-1]
    if new_x[::1] == reverse_new_x:
        pal : bool = True
        print(pal)
        print(f'Пояснение: “{x}” читается, как “{x}” слева направо так и справа налево.')
    else:
        pal: bool = False
        print(pal)
        print(f'Пояснение: слева направо она читается как “{x}” . Справа налево оно становится “{reverse_x}”.')

x = input("x = ")
print(palindrom(x))
