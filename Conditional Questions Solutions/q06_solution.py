
Distance = int(input("How much distance: "))

if Distance < 3:
    print("Walk")
    
elif 3 <= Distance <= 15:
    print("Bike")
    
else:
    print("Car")
