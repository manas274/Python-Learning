def sum_all(*args):
    print(args)
    
    return sum(args) #sum is default method in python

print(sum_all(1,2))
print(sum_all(1,2,3,4,5,6))

# *args allows a function to accept any number of positional arguments, which are collected into a tuple.
# A positional argument is an argument assigned to a function parameter based on its position in the function call.