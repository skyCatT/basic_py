#/usr/bin/python3

letter = list("hello")
print(letter)
print(len(letter))

letter[1] = []
print(letter, len(letter))  #!!attention

letter[1:2] = []
print(letter)

