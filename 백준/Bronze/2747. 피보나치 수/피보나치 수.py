N = int(input())
start = 0
lst = [0, 1]
cnt = 2
while cnt < N + 1:
    plus = lst[start] + lst[start+1]
    lst.append(plus)
    cnt += 1
    start += 1
print(lst[-1])