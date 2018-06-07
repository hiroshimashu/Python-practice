"""
Write a program that accepts a sentence and calculate the number of letters and digits.
"""
sentence = input()
num_letters = 0
num_numbers = 0
"""
Step1. Split sentence into number and letters
"""
for chunk in sentence:
    if chunk.isdigit():
        num_numbers += 1
    elif chunk.isalpha():
        num_letters += 1
    else:
        pass
print("letters", num_letters)
print("digits", num_numbers)
