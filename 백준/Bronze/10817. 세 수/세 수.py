import heapq
number3 = list(map(int,input().split()))
heapq.heapify(number3)
heapq.heappop(number3)
print(number3[0])