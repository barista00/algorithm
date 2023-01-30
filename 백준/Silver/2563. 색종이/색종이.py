N = int(input())
lst = [[0]*100 for _ in range(100)]
for _ in range(N):
    n, m = map(int, input().split())
    for j in range(10):
        for q in range(10):
            lst[m+j][n+q] = 1
plus = 0
for i in lst:
    plus += sum(i)
print(plus)