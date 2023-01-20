taebo = input()
a = 0
for i in taebo:
    if i == '@':
        a += 1
    elif i == '(':
        print(a, end=" ")
        a = 0
print(a)