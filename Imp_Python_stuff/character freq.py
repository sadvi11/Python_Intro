s = "aab"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)  # Output: {'a': 2, 'b': 1}
