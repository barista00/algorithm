a, b, c = list(map(int,input().split()))
num_list = [a, b, c]
if a == b and a == c:
    money = 10000 + a * 1000
elif a == b or b == c:
    money = 1000 + b * 100
elif a == c:
    money = 1000 + a * 100
else:
    num_list.sort()
    money = num_list[-1] * 100
print(money)