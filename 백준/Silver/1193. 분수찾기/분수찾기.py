N = int(input())

분모 = 0
비교할수 = 0
while True:
    분모 += 1
    비교할수 += 분모
    if 비교할수 >= N:
        break
if 분모 % 2 == 0:
    top = 분모 - (비교할수 - N)
    bot = (비교할수 - N) + 1
else:
    top = (비교할수 - N) + 1
    bot = 분모 - (비교할수 - N)
print(f'{top}/{bot}')