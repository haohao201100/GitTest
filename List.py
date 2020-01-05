#List 22.12.2019

word = 'Programming'
word[0]
word[-2]
word[3:5]
word[4:9]
word[:5]
word[8:]
word[5:-3]
word[:2] + word[3:]

len(word)

# Len = Length

square = 'Square'
len(square)
len(word) + len(square)

cube = [10, 20, 30, 45, 50]
cube
cube [3] = 40
cube[5] = 60 #error out of range
cube.append(4*10*20*36)
cube
programA = ['A','B','C','D','E']
>>> programB = ['a','b','c','d','e']
>>> ProgramC = programA + programB
>>> ProgramC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
>>> ProgramD = [1, 2, 3, 4, 5]
>>> ProgramC = ProgramC + ProgramD
>>> ProgramC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5]
>>> ProgramC[9:] = []
>>> ProgramC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd']
>>> ProgramC[5:9] = ProgramD
>>> ProgramC
['A', 'B', 'C', 'D', 'E', 1, 2, 3, 4, 5]

len(ProgramC)

a = [10, 20, 30, 40, 50]
b = [60, 70, 80, 90, 100]
c = [110, 120, 130, 140, 150]
x = [a, b, c]
x

x[0][]
x[][3]
x[1][2]
x[][]
x[0][0]
x[1][1]
x[]

x[1][2] + x[2][0]
x[0][1] - x[2][1]
