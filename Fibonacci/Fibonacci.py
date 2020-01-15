#Fibonacci

#Fibonacci Number Module

# n = int(input('Please enter a nummber: '))

def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end=' ') 
		a, b = b, a+b
	print()

#fib(200)

#Go to Fibonacci Powerpoint

def fib2(n):  #return Fibonacci series up to n
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result

# fib2(200)

# >>> fib #import

# fib(200)