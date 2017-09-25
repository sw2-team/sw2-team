def rf(x):
	if x == 1 or x == 0:
		return 1
	else :
		a = rf(x-1) * x
		return a


while True:

	n = int(input("수를 입력하세요"))
	if n <= -1:
	  	break
	answer = rf(n)

	print(n , "! = " , answer)
