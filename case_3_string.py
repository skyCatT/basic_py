#!/usr/bin/python3

print("it's a \\n")
print('"it\'s a \\n"')
print(r"it's a \n")
print(r"it's a \n")

#--mulitiline
multiline = """it's a
multilien 
content
"""
print(multiline)

#--contenation
v_dog = 3 * 'dog'
v_cat = 3* 'cat'
v_cat_dog = v_dog + v_cat + ' the whole'
print('format 1: %s + %s is %s'%(v_dog, v_cat, v_cat_dog))
print('format 2: {0} + {1} is {2}'.format(v_dog, v_cat, v_cat_dog))

c_1 = 'hello' \
'world' \
'python'

print(c_1[:])
print(c_1[-1])
print(c_1[:-3])
print(c_1[1:4])

#--contenation_v2
nums = '0123456789'
c2 = nums[-2] + nums[2]
c3 = nums[-2:] + nums[2:]
print(c2)
print(c3)


