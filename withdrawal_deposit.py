"""Write a program that computes the net amount of a bank account based a transaction log from console input."""

"""Get the header of input and Decide whether these are W or D"""
net_amount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation ==  "D":
        net_amount += amount
    elif operation == "W":
        net_amount -= amount
    else: 
        pass

print(net_amount)

