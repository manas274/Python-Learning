def even_generator(limit):
    for i in range (2, limit+1, 2):
        yield i  
        # return i
                
for r in even_generator(10):
    print(r)

# yield saves the current state of the function and continue from the next unlike return it ends without continue
# (2, limit+1, 2) last 2 means every step will skip 1 number.
# yield: 
# Returns a value, saves the function’s current state, and continues from where it left off when requested again.
# return: 
# Returns a value and terminates the function.