total_price = int(input())
N = int(input())
plus = 0
for i in range(N):
    money, num = map(int, input().split())
    plus += money*num
if plus == total_price:
    print('Yes')
else:
    print('No')