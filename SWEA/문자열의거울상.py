# 문자열의 거울상
T = int(input())
for t in range(1,1+T):
    st = input()
    lst = []
    for i in st[::-1]:
        if i == 'q':
            lst.append('p')
        elif i == 'p':
            lst.append('q')
        elif i == 'b':
            lst.append('d')
        else:
            lst.append('b')
    print(f'#{t}',end=" ")    
    for i in lst:
        print(i,end="")
    print('')
    
