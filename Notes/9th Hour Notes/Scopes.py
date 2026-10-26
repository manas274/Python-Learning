#Example 01:
# username = "pythonlearning" #global

# def func():
#     username="python"
#     print(username)
    
# print(username)
# func()

#Example 02
# x = 99
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global x # this refers to x = 99
#     x = 12    
# func3()
# print(x)


# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2
# myResult = f1()
# myResult() # () this means EXECUTE in python

#Example 03 (closure)
# def aicoder(num): #outer function
#     def actual(x): #inner function
#         return x ** num
#     return actual


# f = aicoder (2)
# g = aicoder(3)

# print(f)
# print(g)
 
# print(f(3)) # value of x because actual(x) is defined insdie f (aicoder)
# print(g(3)) 

# # f = actual(2) -> this is wrong because actual() is defined inside aicoder(), actual() is not accessible




