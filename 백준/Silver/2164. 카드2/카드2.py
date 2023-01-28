from collections import deque
N = int(input())
lst = deque(range(1, 1+N))
while len(lst) != 1:
    deque.popleft(lst)
    deque.append(lst, deque.popleft(lst))
print(lst[0])