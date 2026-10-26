```markdown

# Scopes
>>>Scope refers to the region of a program where a variable can be accessed.

Python has four types of scope (LEGB):
1. Local: Variables defined inside the current function.

2. Enclosing: Variables defined in an outer function that contains an inner function.

3. Global: Variables defined at the top level of a module.

4. Built-in: Names provided by Python, such as print() and len().

Example:
x = 10  # Global scope

def greet():
    x = 5  # Local scope
    print(x)

greet()
print(x)

Output:
5
10

Explanation:
>>>Inside greet(), the local variable x has the value 5.

>>>Outside the function, the global variable x has the value 10.

>>>The local variable does not change the global variable.

# Closure:
>>>A closure is a function that remembers and can access variables from its enclosing scope, even after the outer function has finished executing.

Example:
def aicoder(num):
    def actual(x):
        return x ** num
    return actual

f = aicoder(2)
g = aicoder(3)

print(f(3))
print(g(3))

Output:
9
27

Explanation:
>>>aicoder(num) is the outer function.

>>>actual(x) is the inner function that uses num from the enclosing scope.

>>>return actual returns the inner function without executing it.

>>>f = aicoder(2) creates a closure that retains access to num = 2.

>>>g = aicoder(3) creates another closure that retains access to num = 3.

>>>f(3) calculates 3 ** 2, which returns 9.

>>>g(3) calculates 3 ** 3, which returns 27.

>>>The inner function can still access num after the outer function has finished executing.

# Key Difference:
>>>Scope determines where a variable can be accessed.

>>>Closure allows a function to retain access to variables from its enclosing scope after the outer function finishes executing.