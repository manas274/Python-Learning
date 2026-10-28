Price = int(input("Enter the price of trouser= "))
Quantity = int(input("Enter the quantity of trousers purchased= "))

Total_Bill = Price * Quantity

if Price and Quantity <= 0:
    
    print("Error")

elif Total_Bill >= 10000:
    Discount = (20 / 100) * Total_Bill
    Final_Price = Total_Bill - Discount
    print("Original Bill= ", Total_Bill)
    print("Discount Amount= ", Discount)
    print("Final Bill= ", Final_Price)
    
elif 5000 <= Total_Bill < 10000:
    Discount = (20 / 100) * Total_Bill
    Final_Price = Total_Bill - Discount
    print("Original Bill= ", Total_Bill)
    print("Discount Amount= ", Discount)
    print("Final Bill= ", Final_Price)    
    
elif Total_Bill < 5000:
    print("No Discount")