from collections import deque
N = int(input())
lst = deque(range(1, 1+N))
em_lst = []
while len(lst) != 1:
    em_lst.append(lst.popleft())
    lst.append(lst.popleft())
print(*em_lst, *lst)