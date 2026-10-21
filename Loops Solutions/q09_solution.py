items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = ["apple", "banana", "orange"]  
for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    