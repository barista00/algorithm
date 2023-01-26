N = int(input())
for _ in range(N):
    string = input()
    a = 0
    lst = []
    for i in string:
        if i == '(':
            lst.append(i)
        else:
            try:
                lst.pop() 
            except:
                a = 1
    if a == 1: 
        print('NO')
    elif lst == []:
        print('YES')
    else:
        print('NO')