num, num2 = input().split()
num = num[::-1]
num2 = num2[::-1]
if int(num) > int(num2):
    print(num)
else:
    print(num2)