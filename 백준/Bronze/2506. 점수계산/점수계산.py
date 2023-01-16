T = int(input())
zoro = list(map(int,input().split()))
count_list = []

for t in range(T):
    if zoro[t] == 0:
        count_list.append(0)
    else:
        if t == 0:
            count_list.append(1)
        elif zoro[t-1] == 0:
            count_list.append(1)
        else:
            count_list.append(count_list[t-1] + 1)
print(sum(count_list))