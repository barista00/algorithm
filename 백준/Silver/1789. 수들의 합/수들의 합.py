N = int(input())
result = 0
cnt = 0
while True:
    result += 1
    cnt = cnt + result
    
    if cnt > N:
        break
print(result-1)