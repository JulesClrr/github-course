text = "Hello World!"

alphabet = "abcdefghijklmnopqrstuvwxyz"

result = {}

for letter in alphabet:
    result[letter] = text.count(letter)

print(result)
