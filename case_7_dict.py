#!/usr/bin/python

fruits = {'D':"apple", 'B':"pear", 'C':"orange"}

print(fruits['D'])
print(list(fruits.keys()))
print(sorted(list(fruits.keys())))

a = dict([("cat", 1), ("dog", 2)])
print(a)

n = 'dog'
b = dict(cat = 1, dog = 2 )
print(b)

print("\n--for")
for i,v in fruits.items():
	print(i,v)
