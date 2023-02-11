import heapq
N = int(input())

lst = []
heapq.heapify(lst)
for _ in range(N):
    num = int(input())
    heapq.heappush(lst, num)

while len(lst) != 0:
    print(heapq.heappop(lst))