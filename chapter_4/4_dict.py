#!/usr/bin/python

#--create
D1 = {"apple":1, "orange":2}
print(D1)
D2 ={}
D2["sky"] = 'blue'
D2['cloud'] = 'white'
D2['wind'] = 'soft'
print(D2) 

#--nesting
D3 = {'name':{"first":"bob", "second":"smith"},
	'job': ['enginerr', 'manager'],
	'age': 40.5}

print(D3)
print('d.name', D3['name'])

c1 = D3['name']['first']
print(c1)

D3['job'].append('janitor')
print(D3['job'])

D3['job'][2:3] = []
print(D3['job'])

#--sort
##
for k in sorted(D2):
	print(k, '-->' , D2[k])
##
sk =  list(D3.keys()).sort()
print(sk) #!-- return none

ks = list(D3.keys())
ks.sort()
print(ks)

#--if test
value = D2.get('addr', 10)
print(value)

v2 = D3['addr'] if 'x' in D3 else 0
print(v2)	













