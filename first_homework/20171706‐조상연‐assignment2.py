def factorial(n):
    while n != -1:
        if n == 0:
            print('0! = 1')
            n = int(input('Enter number: '))
            continue

        factorial_number = n
        for i in range(1, n):  # OR for i in range(n-1, 0, -1):
            factorial_number = factorial_number * i
        print(n,'! = ', factorial_number )
        n = int(input('Enter number: '))


number = int(input('Enter number: '))
factorial(number)
