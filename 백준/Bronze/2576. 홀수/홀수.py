arr = []
for i in range(7):
    num = int(input())
    if num % 2 == 1:
        arr.append(num)
if len(arr) == 0:
    print(-1)
else:
    arr.sort()
    print(sum(arr))
    print(arr[0])