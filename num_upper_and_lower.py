num_lower = 0
num_upper = 0

s = input()
for c in s:
    if c.isupper():
        num_upper += 1
    elif c.islower():
        num_lower += 1

print("UPPER CASE", num_upper)
print("LOWER CASE", num_lower)

