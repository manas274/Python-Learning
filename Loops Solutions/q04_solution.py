input_str = "Python"
reverse_str = ""  # "" , P+"", y+"P" , t+"yP"...

for char in input_str:
    reverse_str = char + reverse_str
    
print(reverse_str, "")