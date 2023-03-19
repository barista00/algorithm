n = int(input())

stair = []
for _ in range(n):
    stair.append(int(input()))

if n < 3:
    print(sum(stair))
    exit()

dp = [] # 값이 가장 큰 최적의 값을 저장한다

dp.append(stair[0])
dp.append(stair[0] + stair[1])
dp.append(max(stair[0] + stair[2], stair[1] + stair[2]))

for i in range(3, n):
    case1 = stair[i] + dp[i-2]
    case2 = stair[i] + stair[i-1] + dp[i-3] # 여기서 stair[i-1]을 한 이유는 i가 3일 때 dp[2]를 더해버리면 앞에서 stair[1]+stair[2]로 초기화된
    dp.append(max(case1, case2))            # 값이 들어있다면 1+2+3의 인덱스값이 더해지기 때문에 조건에 맞지 않게된다
                                            # [i-1], [i-3]을 구할 땐 가중치가 들어오지 않은 경우를 봐야하므로 그냥 stair[i-1]을 넣는다
                                            # 나머지 경우는 한칸 띄어져있기 때문에 가중치가 들어와야한다 (값이 가장 큰 최적의 경로)
                                            # 그 앞에서 구한 값이 가장 최적의 값이기 때문
print(dp[n-1])