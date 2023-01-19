p_number = {
    'ABC': 3, 'DEF': 4, 'GHI': 5,
    'JKL': 6, 'MNO': 7, 'PQRS': 8,
    'TUV': 9, 'WXYZ':10
}
call = list(map(str,input()))
a = 0
for i in p_number:
    for j in call:
        if j in i:
            a = a + p_number[i]
print(a)