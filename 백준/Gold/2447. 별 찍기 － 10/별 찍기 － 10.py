n = int(input())

def f(n):
    if n == 3:
        return ['***', '* *', '***']
    
    return_li = f(n // 3)
    li = []

    for i in return_li:
        li.append(i * 3)
    for i in return_li:
        li.append(i + ' '*(n // 3) + i)
    for i in return_li:
        li.append(i * 3)
    return li
print('\n'.join(f(n))) # 문자열 합치는 join함수 활용
                        # join함수 특징인 각각의 요소사이에 넣을 값을 지정해주고 출력하면 리스트가 풀리면서 지정한 값이 요소사이에 들어간다