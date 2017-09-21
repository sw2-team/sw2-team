def recursivefactorial(x):
	if x == 1 or x == 0:
		return 1
	else :
		a = recursivefactorial(x-1) * x
		return a


while True:

	n = int(input("수를 입력하세요: "))
	if n <= -1:
		break
	answer = recursivefactorial(n)

	print(n,"! = ",answer)
	
