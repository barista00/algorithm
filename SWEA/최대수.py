# 문제 (최대 수 구하기)
T = int(input())
for t in range(1, 1+T):
    numbers = list(map(int,input().split()))
    print(f'#{t} {max(numbers)}')