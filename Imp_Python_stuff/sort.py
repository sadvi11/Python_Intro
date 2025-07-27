#Sort a list in ascending order without using built-in .sort() method.

numbers = [40, 10, 30, 20, 50]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]  # Swap

print("Sorted List:", numbers)
