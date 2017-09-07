le(n !=-1):
    num = 1
    fac_num = int(input("숫자 입력: "))
    for a in range(1,fac_num+1):
        num = a*num

    if (fac_num == -1):
        break

    print(num)
