from collections import deque
N, K = map(int,input().split())
lst = deque(range(1, 1+N))
lst2 = []
while lst:
    for _ in range(K-1):
        deque.append(lst, deque.popleft(lst))
    lst2.append(deque.popleft(lst))
print('<', end="")
for i in lst2:
    if i != lst2[-1]:
        print(i, end=", ")
    else:
        print(i, end="")
print('>')