import math

def circle(r): #шенбер
    if r == "":
        default_radius = 5
        return round(math.pi * math.pow(default_radius, 2), 2)
    else:
        return round(math.pi * math.pow(r, 2), 2)

def circle_area(r):
    if r == "":
        default_radius = 5
        s = math.pi*(pow(default_radius,2))#S = π*(R)**2
        return s
    else:
        ss = math.pi * (pow(r, 2))  # S = π*(R**2)
        return ss
