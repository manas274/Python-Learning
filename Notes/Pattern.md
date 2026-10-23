Pattern programs are commonly used to improve loops, nested loops and logical thinking in python.

Concepts:
1. Outer Loop -> controls rows

2. Inner Loop -> control columns/stars

3. print ("*", end=" ") -> print stars on the same line

>>> By using `end=" "`: Instead of a newline, Python adds a space at the end and leaves the cursor on the same line. Because of this, all stars are printed horizontally on a single line (for example: `* * *`). 

4. print() -> moves to the next line

Key Point: Nested loops are the main concept behind pattern programs.

```markdown
Example:

n = 4 # defines the size of the pattern
for i in range(n): # Total rows
    for j in range(n): # Total stars/columns
        print("*", end=" ") # Printing stars in one line with space
    print() # Move cursor to new line

Output:
* * * * 
* * * * 
* * * * 
* * * * 