#!/usr/bin/python

a = list("abcda")
b = list("12341")

for i,v in enumerate(a):
	print(i, v)

for i,v in zip(a,b):
	print(i,v)
