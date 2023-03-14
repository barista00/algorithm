import math

T = int(input())
for _ in range(T):
    n = int(input())
    prime = [True for _ in range(n+1)] # 에라토스테네스의 체 
    prime[0] = False                    # 2부터 특정 수 n까지 총 소수가 몇개인지??구한다
    prime[1] = False                    # True가 n+1개 들어간 리스트생성 
                                        # 2부터 sqrt(n)+1까지 소수인 수를 찾고 소수면 그 수의 배수를 전부 False처리한다(배수라는 얘기는 약수임)
    for i in range(2, int(math.sqrt(n))+1): # 리스트에 남은 True의 ?번째 수들은 모두 소수이다 2번째 수가 True면 2가 소수라는 얘기
        if prime[i] == True:
            multi = 2
            while n >= multi * i:
                prime[i * multi] = False
                multi += 1
    lst = []
    for i in range(1, n+1):
        if prime[i]:
            lst.append(i)
    lst2 = []
    gap = 10000
    result = 1
    for i in lst:
        for j in lst:
            if i + j == n:
                if i <= j:
                    if gap > j - i:
                        gap = j - i
                        result = i, j
    print(*result)