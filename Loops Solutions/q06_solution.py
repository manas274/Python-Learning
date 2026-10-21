number = 20 #20,19,18.....
factorial = 1 #20, 20*19 ....

while number > 0:
    #factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1
    
print("Factorial= ", factorial)