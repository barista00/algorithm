a, b = input().split()

set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

result_set = set1 - set2

sort_result_set = sorted(result_set, key= lambda x:x)
# print(result_set)
if result_set == set():
    print(0)
else:
    print(len(sort_result_set))
    print(*sort_result_set)