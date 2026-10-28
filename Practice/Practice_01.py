# b) Repeat task (a), but this time take both income and bonus_percent as inputs from the user.

# c) Store the calculated bonus in a new variable called bonus. Create another variable named
# total_income. Add the bonus to your income and store it in total_income. Finally, print the
# updated income.



income = int(input("Enter your monthly income: "))
bonus = int(input("Enter your monthly bonus: "))

Bonus = (bonus / 100) * income
print("monthly bonus= ", round(Bonus,2))

New_bonus = Bonus
total_income = New_bonus + income
print("Total_income= ",total_income)