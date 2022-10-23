def valid_brackets(string):
    bracket_open = ('{', '[', '(')
    bracket_close = ('}', ']', ')')
    select_open = []
    for i in string:
        if i in bracket_open:
            select_open.append(i)
        if i in bracket_close:
            if len(select_open) == 0:
                return False
            index = bracket_close.index(i)
            open_bracket = bracket_open[index]
            if select_open[-1] == open_bracket:
                select_open = select_open[:-1]
            else: return False
    return (not select_open)


str = input('ВВОД: x = ')
print(valid_brackets(str))
