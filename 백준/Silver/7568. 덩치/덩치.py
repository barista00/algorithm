N = int(input())

lst = []
for i in range(N):
    WandH = list(map(int, input().split()))
    lst.append(WandH)

grade_li = []
compare = 0

while compare != N :
    grade = 1
    for i in range(N):
        if lst[compare][0] < lst[i][0] and lst[compare][1] < lst[i][1]:
            grade += 1
    grade_li.append(grade)
    compare += 1
print(*grade_li)