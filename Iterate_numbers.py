class Iterate_numbers(self):
    def __init__(self, range):
        print('Instance has created.')
        
    def iteration(self, n):
        i = 0
        while i < n:
            j = i
            i = i + 1
            if j % 7 == 0:
                yield j