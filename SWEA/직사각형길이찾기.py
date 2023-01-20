# 직사각형 길이 찾기
T = int(input())
for t in range(1,1+T):
    num = list(map(int,input().split()))
    if num[0] == num[1]:
        print(f'#{t} {num[2]}')
    elif num[0] == num[2]:
        print(f'#{t} {num[1]}')
    else:
        print(f'#{t} {num[0]}')
