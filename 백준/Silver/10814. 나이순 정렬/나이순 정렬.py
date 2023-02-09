N = int(input())

lst = []
for _ in range(N):
    age, name = input().split()
    lst.append((int(age), name))
age_sort_lst = sorted(lst, key=lambda x: x[0])

for i in age_sort_lst:
    print(*i)