#Sum of Positive Numbers Until -1 is Entered (While Loop)
total = 0
number = int(input("Enter a number (-1 to stop): "))

while number != -1:
    if number > 0:
        total += number
    number = int(input("Enter a number (-1 to stop): "))

print("Total of positive numbers is:", total)
