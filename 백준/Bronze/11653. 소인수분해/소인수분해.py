n = int(input())
if n == 1:
    exit()

for i in range(2, n+1):
    while True:
        if n % i != 0:
            break
        n = n // i
        print(i)