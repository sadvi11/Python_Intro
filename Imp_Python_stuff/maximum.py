# to find max number
numbers = [15, 48, 22, 97, 63]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum number is:", maximum)
