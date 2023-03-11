ab, sleep, goal = map(int, input().split())
result = (goal - sleep) / (ab - sleep)
if int(result) == result:
    print(int(result))
else: 
    print(int(result) + 1)