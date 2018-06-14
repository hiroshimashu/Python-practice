"""
The numbers after the direction are steps. 
Please write a program to compute the distance from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
"""
import math
x_direction = 0
y_direction = 0


def record_movement(move):
    global x_direction
    global y_direction
    direction = move[0]
    amount = int(move[1])
    if direction == "UP":
        x_direction += amount
    elif direction == "DOWN":
        x_direction -= amount
    elif direction == "LEFT":
        y_direction += amount
    else:
        y_direction -= amount

def calculate_distance(x,y):
    distance = round(math.sqrt(x**2 + y ** 2))
    return distance

while True:
    s = input()
    if s:
        current_direction = [x for x in s.split(" ")]
        record_movement(current_direction)
    else:
        break 
print(x_direction, y_direction)
print(calculate_distance(x_direction, y_direction))
  

