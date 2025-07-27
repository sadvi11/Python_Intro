Numbers = [10, 28, 32, 42, 15, 61, 71, 18, 23, 11]

max_num = Numbers[0]  # Start by assuming the first number is the maximum

for num in Numbers:
    if num > max_num:
        max_num = num  # Update if a bigger number is found

print("The maximum number in the list is:", max_num)
