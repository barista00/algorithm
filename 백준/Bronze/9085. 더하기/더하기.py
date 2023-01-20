T = int(input())
plus = 0
for t in range(1,1+T):
    num = int(input())
    numbers = list(map(int,input().split()))
    for i in numbers:
        plus += i
    print(plus)
    plus = 0