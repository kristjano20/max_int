# Program asks for a number n and then prints out the first n numbers in 
# the sequence (1,2,3,6,11,20,37...)

n = int(input("Enter the length of the sequence: ")) # Do not change this line

counter_int = 3
numa_int = 1
numb_int = 2
numc_int = 3

if n <= 0:
    print("Input must be > 0")
elif n == 1:
    print(numa_int)
elif n == 2:
    print(numa_int,numb_int,sep=', ')
elif n == 3:
    print(numa_int, numb_int, numc_int, sep=', ')
else:
    print(numa_int, numb_int, numc_int,sep='\n')
    prev3sum_int = 0
    while counter_int < n:
        prev3sum_int = numa_int + numb_int + numc_int
        numa_int = numb_int
        numb_int = numc_int
        numc_int = prev3sum_int
        print(prev3sum_int)
        counter_int += 1
    print()
