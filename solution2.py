# Write code for algorithm 2 below
def natural_nums(firstnum, secondnum):
    # Base case
    # If the number we are trying to print is greater than n (secondnum), stop the function.
    if firstnum > secondnum:
        return
        
    else:
        print(firstnum)
        natural_nums(firstnum+1, secondnum)

# natural numbers will always start at 1 and increase as while numbers, 1, 2, 3...
natural_nums(8)