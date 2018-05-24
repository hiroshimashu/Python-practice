# calculate square root of [(2 * C * D)/H]
# Where C and H is constant( C = 50, H = 30) and D is user input of commaceparated value
def main():
    C = 50
    H = 30
    D = input()
    square_root = Square_Root(C, H, D)
    print(square_root)
    return square_root

def Square_Root(c, h, d):
    d = modifyInput(d)
    for i in d:
        sq_root = (2 * c * d[i]) / h
        d[i] = round(sq_root)
    return d

# modify input value into array
def modifyInput(d):
    array_st = d.split(',')
    return array_st

main()
