# "r" - read

# "a" - append

# "w" - Write

# "x" - Create

# "t" - Text

# "b" - Binary

#open & Read File

# f = open('test.txt', 'r') #R - Read

# print(f.name)

# f.close()

# with open('test.txt', 'a') as g:

# 	g.Write('This is line number 6'+"\n")

# 	print(g,end='')

with open('test.txt', 'r') as f:

	# f_text = f.readline()
	# print(f_text,end='')

	# f_text = f.readline()
	# print(f_text,end='')

	# for f_text in f:
	# 	print(f_text,end='')

	# # for line in f:
	# # 	print(line,end='')

	# f_text = f.read(50)
	# print(f_text,end='')

	size_to_read = 10
	f_text = f.read(size_to_read)


	while len(f_text) > 0:
		print(f_text,end='')