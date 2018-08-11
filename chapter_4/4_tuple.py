#!/usr/bin/python

t = ('spam', 3, [1,2,3], {x : x for x in [1,2,3]})
print(t)

#--change mutable element
t[2].append([4,5])
print(t)

t[3]['dog'] = 4
print(t)

#--
##t[1] = 3 !not suport
print(t)
