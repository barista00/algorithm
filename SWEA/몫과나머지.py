# 문제 (몫과 나머지 출력하기)
T = int(input())

for t in range(1, 1+T):
    a, b = list(map(int, input().split()))
    c = a // b
    d = a % b
    print(f'#{t} {c} {d}')