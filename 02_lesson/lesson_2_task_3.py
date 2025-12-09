import math
def square(side):
    result = side * side
    return math.ceil(result)
side_value = 6.7
area = square(side_value)
print(f"Площадь квадрата со стороной {side_value} = {area}")