N = int(input())
checking = set(map(int, input().split()))

M = int(input())
checked = list(map(int, input().split()))

# 만약 checked에 숫자가 checking 세트안에 있으면 1 출력 아니면 0출력
for i in checked:
    if i in checking:
        print(1)
    else:
        print(0)