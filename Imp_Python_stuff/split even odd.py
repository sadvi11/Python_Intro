# split even odd from list
#Use % (modulus) to check if number is even or odd.

numbers = [11, 22, 33, 44, 55, 66]
even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)
