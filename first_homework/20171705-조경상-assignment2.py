while True:

	n = int(input("Enter a number: "))
	f = 1
	if n <= -1:
		exit()
	if n == 0 :
		print("0! = 1")
	if n >= 1 :
		for i in range(1,n+1):
			f = f*i
		print("%d! = %d"%(n,f))

	
	


