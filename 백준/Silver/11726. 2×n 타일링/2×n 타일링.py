n = int(input())
dp = [0, 1, 2]

def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    for i in range(3, n+1):
        new_index = dp[i - 1] + dp[i - 2]
        dp.append(new_index)
    return dp[n]
print(f(n) % 10007)