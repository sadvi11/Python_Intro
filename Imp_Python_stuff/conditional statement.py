# Ask user to enter their age
age = int(input("Enter your age: "))

# Conditional statements to determine ticket price
if age < 5:
    print("You get a free ticket!")
elif age >= 5 and age < 18:
    print("You pay a child ticket price: $5")
elif age >= 18 and age < 60:
    print("You pay an adult ticket price: $12")
else:
    print("You pay a senior ticket price: $8")
