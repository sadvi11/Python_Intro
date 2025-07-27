a = [1, 2]
b = [3, 4]

a.append(b)
print(a)  # Output: [1, 2, [3, 4]]

a = [1, 2]
a.extend(b)
print(a)  # Output: [1, 2, 3, 4]
