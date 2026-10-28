import math

Required = str(input("Choose R or T or C: "))
if Required == "R":
    Length = int(input("Enter the length of rectangle= "))
    Width = int(input("Enter the width of rectangle= "))
    Perimeter_of_Rectangle = Length * 2 + Width * 2
    print("perimeter_of_rectangle= ", Perimeter_of_Rectangle)
    Area_of_Rectangle = Length * Width
    print("area_of_rectangle= ", Area_of_Rectangle)
    
elif Required == "T":
    a = int(input("Enter the length of side a= "))
    b = int(input("Enter the length of side b= "))
    c = int(input("Enter the length of side c= "))
    base = int(input("Enter the base= "))
    height = int(input("Enter the height= "))
    Perimeter_of_Triangle = a + b + c
    print("perimeter_of_triangle= ", Perimeter_of_Triangle)
    Area_of_Triangle = 0.5 * base * height 
    print("area_of_triangle= ", Area_of_Triangle)
    
    
elif Required == "C":
    r = int(input("Enter the radius of circle= "))
    Circumference_of_Circle = 2 * math.pi * r
    c = Circumference_of_Circle
    print("circumference_of_Circle= ", round(c,4))
    
    Area_of_Circle = math.pi * r**2
    a = Area_of_Circle
    print("area_of_circle= ", round(a,4))
    
else:
    print("The entered value is invalid")
    
    
    