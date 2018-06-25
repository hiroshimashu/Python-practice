from Stack import Stack

def parenthesis_checker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString[index]) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

ans = parenthesis_checker("(((())")
print(ans)
    