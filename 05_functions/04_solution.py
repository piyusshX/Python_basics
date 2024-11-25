import math
def circle_stats(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    # in python we can return more than 1 value
    return area, circumference, "hi"

a, c = circle_stats(3)

print("Area :", a, "\nCircumference :", c)