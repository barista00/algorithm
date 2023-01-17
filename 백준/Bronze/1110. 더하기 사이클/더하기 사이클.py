N = input()
N_int = int(N)
count = 0
while True:
    a = N_int % 10
    b = N_int // 10 + N_int % 10
    compare = (a * 10) + (b % 10)
    count += 1
    if str(compare) == N:
        break
    else:
        N_int = compare
print(count)