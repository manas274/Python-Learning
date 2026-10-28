income = int(input("Enter your monthly income: "))
bonus = int(input("Enter your monthly bonus: "))

Bonus = (bonus / 100) * income
print("monthly bonus= ", round(Bonus,2))

New_bonus = Bonus
total_income = New_bonus + income
print("Total_income= ",total_income)