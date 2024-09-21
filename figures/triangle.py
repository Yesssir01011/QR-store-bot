import math

def triangle_perimeter (a,b,c):
    if a == "" and b == "" and c == "":
        a = 7
        b = 2
        c = 8
        p = a+b+c #периметр формуласы
        return p
    else:
        g = a+b+c
        return g


def triangle_area(a,b,c):
    if a == "" and b == "" and c == "":
        a = 7
        b = 2
        c = 8
        s = math.sqrt(triangle_perimeter(a,b,c)*((triangle_perimeter(a,b,c)-a)*(triangle_perimeter(a,b,c)-b)*(triangle_perimeter(a,b,c)-c)))  # аудан формуласы
        return s
    else:
        ss = math.sqrt(triangle_perimeter(a,b,c)*((triangle_perimeter(a,b,c)-a)*(triangle_perimeter(a,b,c)-b)*(triangle_perimeter(a,b,c)-c)))
        return ss


