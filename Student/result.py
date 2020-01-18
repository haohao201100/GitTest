import student
import mary

x = student.a['age']
y = student.a['father']
z = student.b['age']
v = student.b['mother']
print(x, y, ' ', z, v)

for i in range(len(mary.a)):
	print(i, mary.a[i])