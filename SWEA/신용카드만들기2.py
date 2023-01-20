# 신용카드 만들기 2
T = int(input())
req = ['3','4','5','6','9']
number = ['1','2','3','4','5','6','7','8','9','0']
for t in range(1,1+T):
    card = input()
    cnt = 0
    if card[0] not in req:
        print(f'#{t} 0')
    else:
        for i in card:
            if i in number:
                cnt += 1
        if cnt != 16:
            print(f'#{t} 0')
        else:
            print(f'#{t} 1')
