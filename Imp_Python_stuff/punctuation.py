#Remove Punctuation
sentence = input("Enter a sentence: ")
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
cleaned = ""

for char in sentence:
    if char not in punctuations:
        cleaned += char

print("Without punctuation:", cleaned)
