Name = str(input("Enter your name: "))
Consumption = int(input("Enter your monthly electricity consumption= "))

if Consumption < 0:
    print("Error")
    
elif 1 <= Consumption <= 100:
    Montly_Bill = 10 * Consumption
    print("montly_bill= ", Montly_Bill)
    
elif 101 <= Consumption <= 200:
    Montly_Bill = 15 * Consumption
    print("montly_bill= ", Montly_Bill)
    
elif Consumption > 200:
    Montly_Bill = 20 * Consumption
    print("montly_bill= ", Montly_Bill)