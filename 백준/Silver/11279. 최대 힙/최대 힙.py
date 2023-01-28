import heapq, sys
lst = []
heapq.heapify(lst)
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(lst, -num)
    else:
        if lst:
            print(-heapq.heappop(lst))
        else:
            print(0)