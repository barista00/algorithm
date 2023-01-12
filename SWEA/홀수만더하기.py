T = int(input())

# 2 나누고 나머지 1이면 홀수
add_list = []
for t in range(1, 1+T):
    numbers = list(map(int, input().split()))
    for i in numbers:
        if i % 2:
            add_list.append(i)
    print(f'#{t} {sum(add_list)}')
    add_list = []