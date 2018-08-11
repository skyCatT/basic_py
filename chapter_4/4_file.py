#!/usr/bin/python

f = open('d2.txt', 'r')
txt = f.read()
print(txt)
stxt = txt.split('\n')
print(stxt)


wf = open('td.txt', 'w')
wf.write('hello\n')
wf.write('world\n')
wf.close()

rf = open('td.txt')
t = rf.read()
print(t)
