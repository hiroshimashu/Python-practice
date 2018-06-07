for i in range(1000, 1100):
    """step1. Find every digit of i is even"""  
    every_digit = [int(l) for l in str(i)]
    digit_divided_by_2 = list(map(lambda x: x % 2, every_digit))

    