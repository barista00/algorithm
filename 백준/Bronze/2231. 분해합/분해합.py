N = int(input())
plus = 0
lst = []
for i in range(1, N):
    for j in str(i):
        plus += int(j)
    if i + plus == N:
        lst.append(i)
    plus = 0
if lst :
    print(min(lst))
else:
    print(0)