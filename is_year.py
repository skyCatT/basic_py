#!/usr/bin/python

year = int(input("input a year"))
re_is = False
if(year % 4 == 0):
	if(year % 100 == 0):
		if(year % 400 == 0):
			re_is = True

if(True == re_is):
	print("satisfy")
else:
	print("no satisfy")
