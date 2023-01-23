lst = list(range(1,31))
blank_lst = []
result_lst = []
for i in range(28):
    student = int(input())
    blank_lst.append(student)
for i in lst:
    if i not in blank_lst:
        result_lst.append(i)
result_lst.sort()
print(result_lst[0],'\n', result_lst[1], sep="")