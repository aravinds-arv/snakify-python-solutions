def distance(x1, y1, x2, y2):
    import math
    dx = (x2-x1)
    dy = (y2-y1)
    distance = math.sqrt((dx**2) + (dy**2))
    return distance

print(distance(float(input()), float(input()), float(input()), float(input())))