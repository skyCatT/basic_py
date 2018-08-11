#!/usr/bin/python

M = [[1, 2, 3],[1,2,3]]
r1 = [row[1]  for row in M]
print(r1)
r2 = [i * i for i in [1,2,3]]
print(r2)
r3 = [i * 2 for i in 'spam']
print(r3)
r4 = {i:i*i for i in [1,2,3]}
print(r4)


##
#--
G = (sum(row) for row in M)
print(next(G))
print(next(G))
#--
sumrow = list(map(sum, M))
print(sumrow)



