# Print a Box
# Given a height and width, input by the user, print a box consisting of * characters as its border. Example session:

# $ python box.py
# Width? 6
# Height? 4

width = int(raw_input("Width? "))
height = int(raw_input("Height? "))

for char in range(height):
    if char in (0, height-1):
        char = '*'
        print char*width
    else:
        char = '*'
        print char + ' '*(width-2) + char