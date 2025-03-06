from math import cos, sin

TOP = 1
DOWN = 0

def transform(center, angle, relative_point):
    x, y = relative_point
    x0, y0 = center
    x1 = x0 + x * cos(angle) - y * sin(angle)
    y1 = y0 + x * sin(angle) + y * cos(angle)
    return (x1, y1)