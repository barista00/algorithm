# if문 사용할 때 많이 적으려면 일단 소거법 느낌으로 False출력을 먼저해서 하나하나씩 걸러내듯 적으면 그나마 괜찮음
# tuple전환시 int에서 튜플은 안되고 string에서 튜플은 되더라
T = int(input())
p = -1
for t in range(1,1+T):
    date = tuple(input())
    date_list = list(map(int,date))
    if date_list[4] not in [0,1]:
        print(f'#{t} {p}')
    else:
        if date_list[4] == 1 and date_list[5] > 2 or date_list[5] == 0:
            print(f'#{t} {p}')
        else:
            if date_list[4] == 0 and date_list[5] == 2 and date_list[6] > 2 or date_list[7] > 8:
                print(f'#{t} {p}')
            else:
                if date_list[6] > 3 :
                    print(f'#{t} {p}')
                else:
                    if date_list[6] == 3 and date_list[7] > 1:
                        print(f'#{t} {p}')
                    else:
                        date_list = list(map(str, date_list))
                        date_list.insert(4,'/')
                        date_list.insert(7,'/')
                        c = ''.join(date_list)
                        print(f'#{t} {c}')
