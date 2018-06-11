"""A website requires the users to input username and password to register. Write a program to check the validity of password input by users."""
import re
value = []
items = [x for x in input().split(",")]
for p in items:
    if len(p) < 6 or len(p) > 12:
        continue
    elif not re.search("[0-9]", p):
        continue
    elif not re.search("[A-Z]", p):
        continue
    elif not re.search("[$#@]", p):
        continue
    elif re.search("\s", p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))



