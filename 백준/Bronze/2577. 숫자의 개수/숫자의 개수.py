cal_num = 1
for i in range(3):
    num = int(input())
    cal_num = cal_num * num
num_dict = {
    '0':0,'1':0,'2':0,'3':0,
    '4':0,'5':0,'6':0,'7':0,
    '8':0,'9':0
}
str_cal_num = str(cal_num)
a = 0
for i in str_cal_num:
    if i in num_dict:
        num_dict[i] = num_dict[i] + 1
for i in num_dict:
    print(num_dict[i])