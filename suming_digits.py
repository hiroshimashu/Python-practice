s = input()
digit_sum = 0
for i in range(1, 5):
    digit_sum += int(str(s) * i)

print(digit_sum)