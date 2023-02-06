N = input()
N = list(N)
hap = 0
unhap = 0
# ':'가 등장하는지 확인하는 코드
for i in range(len(N)):
    if N[i] == ':':
        # N[i]가 ':'라면 뒤에 2개가 -) -( 둘중 어떤건지 확인하고 카운트
        if N[i:i+3] == [':','-',')']:
            hap += 1
        elif N[i:i+3] == [':','-','(']:
            unhap += 1

# 개수에 따라 조건을 적용해 출력
if hap > unhap:
    print('happy')
elif unhap > hap:
    print('sad')
elif unhap == 0 and hap == 0:
    print('none')
elif unhap == hap:
    print('unsure')