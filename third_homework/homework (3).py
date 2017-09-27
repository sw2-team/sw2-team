def recursive_factorial(x):
    if x==0:
        return 0

    if x == 1:
        return 1
    else: 
        return recursive_factorial(x-1)*x

while True:

	n = int(input("수를 입력하세요: "))
	if n < 0:
		break
	answer = recursive_factorial(n)

	print(n,"! = ",answer)
