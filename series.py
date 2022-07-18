##  2**(1) + 2**(2) + 2**(3) + ...... + 2**(n)


length_of_n = int(input("Enter length : "))
sum_of_series  = 0
for one_power in range(1, length_of_n + 1):
    sum = 2**one_power
    sum_of_series += sum
    
print("The sum of series the base is 2 : ", sum_of_series)