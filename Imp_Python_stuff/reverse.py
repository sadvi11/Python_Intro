# reverse a list
numbers = [1, 2, 3, 4, 5]
reversed_list = []

for i in numbers:
    reversed_list = [i] + reversed_list

print("Reversed List:", reversed_list)

