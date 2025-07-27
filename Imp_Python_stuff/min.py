Numbers = [10, 28, 32, 42, 15, 61, 71, 18, 23, 11]

min_num = Numbers[0]

for num in Numbers:
    if num < min_num:
        min_num = num

print("The minimum number in the list is:", min_num)
