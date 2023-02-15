N, M = map(int, input().split())

listen = set()
for _ in range(N):
    listen.add(input())

look = set()
for _ in range(M):
    look.add(input())

result = listen & look
sort_result = sorted(result, key=lambda x : x)
print(len(result))

for i in sort_result:
    print(i)