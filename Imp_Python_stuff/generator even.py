def even_gen(n):
    for i in range(2, n+1, 2):
        yield i

for val in even_gen(10):
    print(val, end=' ')  # Output: 2 4 6 8 10
