```markdown
# Functions Notes

>>>Parameter:
A parameter is a variable defined in a function that receives a value when the function is called.

>>>Argument:
An argument is the actual value passed to a function when calling it.

>>>Default parameter value:
A default parameter value is used when no argument is provided for that parameter.

>>>Positional Arguments:
A positional argument is assigned to a function parameter based on its position in the function call.

Example:
def greet(name, power):
    print(name, power)

greet("Gun", "Anas")

Output:
Gun Anas

>>> Keyword Arguments:
A keyword argument is an argument passed to a function using the parameter's name.

Example:
def greet(name, power):
    print(name, power)

greet(name="Anas", power="Gun")

Output:
Anas Gun

>>>Lambda Function:
A lambda is a small anonymous function that contains a single expression.

Example:
1. Normal function:

def square(x):
    return x * x

print(square(5))

Output:
25

2. Same function using lambda:

square = lambda x: x * x

print(square(5))

Output:
25

>>>*args — Variable Positional Arguments:
*args allows a function to accept any number of positional arguments, which are collected into a tuple.

>>>**kwargs — Variable Keyword Arguments:
**kwargs allows a function to accept any number of keyword arguments, which are collected into a dictionary.

>>>yield:
Produces the current value and pauses the generator, preserving its state until the next value is requested.

>>>yield vs return:
yield: Produces a value, pauses the generator, and allows it to continue from where it stopped when another value is requested.

return: Returns a value and terminates the function.

1. return example:
def normal_function():
    return 2
    return 4

print(normal_function())

Output:
2

>>>The second return is never executed because the function has already terminated.

2. yield example
def generate_numbers():
    yield 2
    yield 4

for number in generate_numbers():
    print(number)

Output:
2
4

>>>The generator produces both values on successive requests.

>>>Recursive Functions:
A recursive function is a function that calls itself to solve a problem.