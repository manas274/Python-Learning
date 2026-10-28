Number = int(input("Enter a number: "))

last_digit = str(Number)[-1]

if int(last_digit) % 3 == 0:
    print("Last digit is divisible by 3")
else:
    print("Last digit is not divisible by 3")
    