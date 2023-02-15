from collections import Counter
import sys

N = int(input())
li = []

for _ in range(N):
    string = input()
    li.append(string)

counter = Counter(li)
num_li = []
for i in counter:
    num_li.append(counter[i])

sort_counter = sorted(counter.items(), key=lambda x : (x[1], x[0])) # 개수 작은 것부터 큰 순으로 정렬하면서 사전 순으로 앞에 오는순

for i in sort_counter: # 개수가 가장 크면서 사전순으로 맨앞에 있는 경우를 출력함
    if i[1] == max(num_li):
        print(i[0])
        break