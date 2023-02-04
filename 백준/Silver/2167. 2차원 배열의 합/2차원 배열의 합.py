N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

K = int(input())
for k in range(K):
    a, b, x, y = map(int, input().split())

    plus_j = 0
    for i in lst[a-1:x]:
        for j in i[b-1:y]:  
            plus_j += j
    print(plus_j)