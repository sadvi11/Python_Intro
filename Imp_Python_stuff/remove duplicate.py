# to remove duplicate 
items = [1, 2, 2, 3, 4, 4, 5]
unique = []

for i in items:
    if i not in unique:
        unique.append(i)

print("Unique list:", unique)
