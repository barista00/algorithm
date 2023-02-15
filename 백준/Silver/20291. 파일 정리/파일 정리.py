from collections import Counter
N = int(input())

lst = []
for _ in range(N):
    not_mean, answer = input().split('.')
    lst.append(answer)

counter = Counter(lst)
sort_counter = sorted(counter.items(), key=lambda x:x[0])

for i in sort_counter:
    print(*i)