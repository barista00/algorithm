# 신용카드만들기 1
T = int(input())
for t in range(1,1+T):
    ca_num = list(map(int,input().split()))
    cnt = 0
    cnt2 = 0
    a = 1
    for i in ca_num :
        if a % 2 == 0:
            cnt += i
            a += 1
        else:
            cnt += (i * 2)
            a += 1
    result = (cnt + cnt2) % 10
    if result == 0:
        print(f'#{t} 0')
    else:
        print(f'#{t} {10-result}')
