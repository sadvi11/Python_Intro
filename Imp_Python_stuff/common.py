#Find elements that appear in both lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []

for item in list1:
    if item in list2:
        common.append(item)

print("Common elements:", common)
