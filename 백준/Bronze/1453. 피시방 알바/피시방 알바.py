from collections import deque
N = int(input())
count = 0
count2 = 1
cus = deque(map(int,input().split()))
first_cus = []
while True:
    try:
        if cus[0] in first_cus:
            count += 1
        first_cus.append(cus.popleft())
    except:
        break
print(count)