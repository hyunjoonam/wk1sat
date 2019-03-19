thing = 1
if type(thing) == int:
    print "%r is an integer." % thing
elif type(thing) == str:
    print "%r is a string." % thing
elif type(thing) == bool:
    print "%r is a boolean." % thing
elif type(thing) == float:
    print "%r is a float." % thing

numbers = [1, 2, 3]
for number in numbers:
    print number

for number in range(10):
    print number

for char in 'Hello':
    print char