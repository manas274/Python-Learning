def greet(name = "Anas"):
    return "Hello, " + name + "!"

print(greet("anas"))


# if "anas" this is not define then it will print the default name "Anas"
# Strings are immutable, meaning their characters cannot be changed, but a variable can be assigned a different string.
# - Parameter: name — the variable defined in the function.
#- Argument: "anas" — the value passed to the function in greet("anas").
# "Anas" is the default parameter value, used when you call greet() without providing an argument.