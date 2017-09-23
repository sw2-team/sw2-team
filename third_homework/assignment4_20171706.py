import time                 #time모듈로 재귀함수와 for loop의 차이를 알아보자!

def recursive_factorial(n):     #재귀함수로 짜여진 팩토리얼 계산
    if n==0:
        return '0!=1'

    if n == 1:
        return 1
    else:
        return recursive_factorial(n-1)*n



def for_loop_factorial(n):      #for loop으로 짜여진 팩토리얼 계산
    if n==0:
        return '0!=1'

    fac_num = n
    for i in range(1,n):
        fac_num = fac_num*i

    return fac_num

#time 모듈로 둘의 차이를 알아보자!
ts=time.time()
print(recursive_factorial(10))
ts= time.time() - ts
print(ts)

ts=time.time()
print(for_loop_factorial(10))
ts= time.time() - ts
print(ts)
