# dp(최대비용) = [0, 1, 2의최대비용, 3의최대비용, ...]
n = int(input())
li = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + li[j]) # 각 dp인덱스별 최대비용 + 그냥비용리스트
print(dp[n])                                   # n이 3이라면 dp[3]을 구할 때 2의최대비용+1의비용, 1의최대비용+2비용, 0의최대비용+3의비용을 구하게된다 