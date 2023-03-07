T = int(input())
second = [300, 60, 10]
result = []
if T % 10 != 0:
    print(-1)
    exit()
for i in range(3):
    result.append(T // second[i])

    T = T % second[i]
print(*result)