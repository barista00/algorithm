station = [list(map(int,input().split())) for _ in range(4)]

start = station[0][1] 
people = [station[0][1]]

for i in range(1,4):
    start = start - station[i][0]
    people.append(start)
    start = start + station[i][1]
    people.append(start)
print(max(people))