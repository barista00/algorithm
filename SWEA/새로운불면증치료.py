T = int(input())
for t in range(1, 1+T):
    a = {0,1,2,3,4,5,6,7,8,9}
    b = {}
    g = set(b)
    k = 1 

    N = input()
    while len(a) != len(g):
        for i in N:
            g.add(int(i))
        N = int(N)//k
        k += 1
        N = int(N)*k
        N = str(N)
    N = int(N)/k
    answer_N = int(N)
    final_N = answer_N*(k-1)
    
    print(f'#{t} {final_N}')




