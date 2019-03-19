# Print a Square II
# Print a NxN square of * characters. Prompt the user for N. Example output:

# $ python square2.py
# How big is the square? 10

howBig = int(raw_input("How big is the square? "))

for char in range(howBig):
    char = '*'
    print char*howBig