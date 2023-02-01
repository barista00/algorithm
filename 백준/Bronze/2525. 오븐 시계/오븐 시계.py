H, M = map(int, input().split())
mi = int(input())
if mi + M < 60:
    M = mi + M
else:
    H = H + ((mi + M) // 60)
    M = (mi + M) % 60

if H > 23:
    H = H % 24
print(H, M)