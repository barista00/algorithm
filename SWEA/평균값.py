# 문제 (평균값 구하기)
T = int(input())
a = 0
for t in range(1, 1+T):
    numbers = list(map(int, input().split()))
    for i in numbers:
        a = a + i
        b = round(a/len(numbers))
        a = 0
    print(f'#{t} {b}')