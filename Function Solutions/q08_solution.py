def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
    
print_kwargs(name="anas", power="gun")
print_kwargs(name="ronaldo")
print_kwargs(name="john", power="lazer", enemy = "Dr. Jackaal")

# **kwargs allows a function to accept any number of keyword arguments, which are collected into a dictionary.
# **kwargs makes dictionary, .items() return key-value pairs, and for loop process pairs one by one.