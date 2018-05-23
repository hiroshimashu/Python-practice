"""
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.

"""

def mult_array(num_row, num_column):
    matrix = []
    row = None
    for i in range(num_row):
       row = [i * j for j in range(num_column)]
       matrix.append(row)
    return matrix

print(mult_array(1, 1))
print(mult_array(3, 5))

