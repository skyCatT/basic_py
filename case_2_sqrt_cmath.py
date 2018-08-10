# -*- coding: UTF-8 -*-
#!/usr/bin/python
import cmath

num = int(input("input a num"))
re = cmath.sqrt(num)
print("{0} is sqrt is {1:0.3f} + {2:0.4f}".format(num, re.real, re.imag))

