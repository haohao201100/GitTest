#Sets

#includes a data type for sets.
#Curly braces or the set() function can be used to create sets.

basket = {'apple', 'orange', 'apple', 'orange', 'banana'}
print(basket)

'orange' in basket
'crabgrass' in basket

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a
a - b
a | b
a & b
a ^ b

a = {x for x in 'abracadabra' if x not in 'abc'}
a

a = {x,y for x in 'abracadabra' if x not in 'abc'}
a


--------------------------

fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)

fruits.add("cucumber")
fruits
fruits.update("grape", "water melon")
fruits
fruits.remove("banana")
fruits
fruits.discard("kiwi")
fruits


>>>Dictionaries

#Dictionaries

#Another useful data type built into Python is the dictionary

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

del tel['sape']
tel['irv'] = 4127
tel

list(tel)

sorted(tel)

'guido' in tel

'sape' not in tel


dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

{x: x**2 for x in (2, 4, 6)}
{x: x**3 for x in (1, 2, 3, 4, 5)}

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k,v)


for i,v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)

questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('What is your {0}? It is {1}.'.format(q, a))