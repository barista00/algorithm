import math
m = int(input())
n = int(input())

def primenumber(k):
    for j in range(2, int(math.sqrt(k))+1):
        if k % j == 0:
            return False
    return True

plus = 0
min_pn = 0 
for i in range(m, n+1):
    if i == 1:
        continue
    if primenumber(i):
        if plus == 0:
            min_pn = i
        plus += i

if plus == 0:
    print(-1)
    exit()
print(plus)
print(min_pn)