import math
n = int(input())
n_list = list(map(int, input().split()))
cnt = 0

def primeNumber(k):                         # 소수가 아닌 약수의 특성상 가운데 약수를 기준으로 곱셈연산이 대칭을 이룬다
    for j in range(2, int(math.sqrt(k))+1): # math모듈의 sqrt함수 인자값에 루트를 씌운다
        if k % j == 0:                      # 예를 들어 16이면 1 2 4 8 16 인데 이중 제곱근인 4까지만 봐도 소수인지 아닌지 알 수 있다
                                            # 쓰는 이유
            return False                    # 만약 반복문도는 숫자가 소수로 입력받은 경우 중간 리턴이 발생하지않고 첨부터 끝까지 다 봐야하기 때문에
    return True                             # 소수인 수를 고려해서 시간복잡도를 줄이는 방법이다
                                            # 즉 소수가 들어와도 11이라면 루트11 + 1 까지만 확인해봐도 소수인지 아닌지 알수가있다
for i in n_list:
    if i == 1:
        continue
    if i == 2:
        cnt += 1
    else:
        if primeNumber(i):
            cnt += 1
print(cnt)