N = input()
lst = []
while True:
    problem = input()
    if problem == '고무오리 디버깅 끝':
        break
    else:
        if problem == '문제':
            lst.append(problem)
        else:                       # 고무오리 들어온경우
            if '문제' not in lst:  # 문제가 없는데 고무오리가 들어온 경우
                lst.append('문제')
                lst.append('문제')
            else:                   # 문제 있는데 고무오리 들어온 경우
                lst.pop()
if '문제' in lst:
    print('힝구')
else:
    print('고무오리야 사랑해')