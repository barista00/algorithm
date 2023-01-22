lst = []
for i in range(10):
    num = int(input())
    lst.append(num % 42)
set_lst = set(lst)
print(len(set_lst))