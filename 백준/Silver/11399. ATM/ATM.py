N = int(input())
minute = list(map(int, input().split()))

minute.sort()
min_minute = minute[0]
result = min_minute
for i in range(1, len(minute)):
    min_minute += minute[i]
    result = result + min_minute  
print(result)