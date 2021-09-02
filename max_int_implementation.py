#Program accept positive numbers and keeps a track of the largest one
#Program stops running when a negative number is input and returns the
#largest positive number input if a positive number was input

max_int = 0
num_int = 0
counter_int = -1

while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))    # Do not change this line
    counter_int += 1

if counter_int == 0:
    print("No positive number received, no maximum available")
else:
    print("The maximum is", max_int)    # Do not change this line
