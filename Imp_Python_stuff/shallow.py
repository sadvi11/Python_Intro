import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)       # shallow
c = copy.deepcopy(a)   # deep

a[0][0] = 100

print(b)  # [[100, 2], [3, 4]] ❌ affected
print(c)  # [[1, 2], [3, 4]] ✅ safe
