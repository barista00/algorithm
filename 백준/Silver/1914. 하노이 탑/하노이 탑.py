def hanoi(n, start, end, goal):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, goal, end)
        print(start, end)
        hanoi(n-1, goal, end, start)

N = int(input())
print(2**N - 1)
if N <= 20:
    hanoi(N, 1, 3, 2)