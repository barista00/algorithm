T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    a = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                for q in lst[i:]:
                    if q[j] == 0:
                        a += 1
                    
    print(a)