input_lst = list(map(int,input().split()))
lst = [1,2,3,4,5,6,7,8]
if input_lst == lst:
    print('ascending')
elif input_lst == lst[::-1]:
    print('descending')
else:
    print('mixed')