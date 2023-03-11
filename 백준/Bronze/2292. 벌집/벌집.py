N = int(input())
cnt = 1
maxnum = 1
while True:
    if N <= maxnum:
        break
    num = 6 * cnt
    maxnum = maxnum + num  
    cnt += 1
print(cnt)