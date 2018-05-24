def integral_number(x):
    pairs = []
    for i in range(1, x + 1):
        integral = i * i
        a_pair = (i, integral)
        pairs.append(a_pair)
    print(dict(pairs))

integral_number(8)
