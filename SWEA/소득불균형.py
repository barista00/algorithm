# 소득불균형
# 입력받은 수 평균 구하기 
T = int(input())
for t in range(1,1+T):
    head = int(input())
    binbu = list(map(int,input().split()))
    plus = sum(binbu)
    aver = plus/head
    cnt = 0
    for i in binbu:
        if i <= aver:
            cnt += 1
    print(f'#{t} {cnt}')
