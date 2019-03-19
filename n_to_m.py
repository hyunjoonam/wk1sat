# $ python n_to_m.py
# Start from: 2
# End on: 8
# 2345678

startNumber = int(raw_input("Enter the number to start on "))
endNumber = int(raw_input("Enter the number to end on "))

for number in range(startNumber, endNumber+1):
    print number