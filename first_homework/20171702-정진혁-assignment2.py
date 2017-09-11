n = 1
while(n != -1):
    num = 1
    fac_num = int(input("숫자 입력: "))
    for a in range(1,fac_num+1):
        num *= a

    if (fac_num <= -1):
        break

    print(num)
