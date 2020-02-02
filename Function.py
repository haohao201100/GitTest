def say_hello():
	print('Hello World')

say_hello()

#function_parameter

def print_max(a,b):
	if a > b:
		print(a, 'is maxium')
	elif a == b:
		print(a,' is equal to'. b)
	else:
		print(b,'is maxium')

print_max(3, 4)

x = 8
y = 11

print_max(x, y)

#Local Variables

def func(x):
	print('x is', x)
	x = 2
	print('Changed local x to', x)

x = 50
func(x)
print('x is still', x)

======

x = 30

def func(x):
    x = 2
    print('x is', x)

def funx(x):
	x = 10
    print('x is', x)

func(x)
funx(x)
x

==========

#Global Statement

def func():
	global x

	print('x is', x)
	x = 2
	print('Changed global x to', x)

x = 50
func()
print('Value of x is', x)

=======

#Default Argument Values

def say(message, times=1):
	print(message * times)

say('Hello')
say('World', 5)
say('Good Bye')


#Keyword Arugment

def func(a, b=5, c=10):
	print('a is', a, 'and b is', b, 'and c is', c)

func(3, 8)
func(24, c=26)
func(c=29, a=39)

#VarArgs parameters
#Function_VarArgs.py

def total(a=5, *numbers, **phonebook):
	print('a', a)

	for single_item in numbers:
		print('single_item', single_item)

	for first_part, second_part in phonebook.items():
		print(first_part, second_part)

total(10, 1, 2, 3, Jack=1123, John=2232, Inge=1459)

#Return Statement

def maximum(x, y):
	if x > y:
		return x
	elif x == y:
		return 'The numbers are equal'
	else:
		return y

print(maximum(3,8))

print(maximum(20, 10))