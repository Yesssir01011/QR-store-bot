#1
"""from math import sqrt
def f(n):
    return (sqrt(n)+n)/2
while True:
    k = input("Программаны тоқтату үшін k жаз:")
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    x = f(a) + f(b) + f(c)
    if k == "k":
        break
    else:
        print("х өрнегінің мәні:",x)
        continue
print("Программа аяқталды!")"""
#2
"""from  math import sin
def sinus(n):
    return (sin(n)+n)/3
while True:
    x = input("Программаны тоқтату үшін x жаз:")
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    y = sinus(a)+sinus(b)+sin(c)
    if x == "x":
        break
    else:
        print("х өрнегінің мәні:",y)
        continue
print("Программа аяқталды!")"""
#3
"""def maximum(a,b):
    return (max(a,2*b)+max((2*a)-b,b))
while True:
    x = input("Программаны тоқтату үшін x жаз:")
    c = int(input("a:"))
    f = int(input("b:"))
    m = maximum(c,f)
    if x == "x":
        break
    else:
        print("х өрнегінің мәні:",m)
        continue
print("Программа аяқталды!")"""
#4
"""from math import sqrt
def xmani(j):
    return (sqrt(j)+j)
while True:
    y = input("Программаны тоқтату үшін y жаз:")
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    d = int(input("d:"))
    f = int(input("f:"))
    g = int(input("g:"))
    x = (xmani(a)/xmani(b))+(xmani(c)/xmani(d))+(xmani(f)/xmani(g))
    if y == "y":
        break
    else:
        print("х өрнегінің мәні:",x)
        continue
print("Программа аяқталды!")"""
#5
"""from math import sin
def ymani(a,b):
    return ((a+sin(a))/(sin(b)+b))
while True:
    x = input("Программаны тоқтату үшін x жаз:")
    l = int(input("a:"))
    m = int(input("b:"))
    c = int(input("c:"))
    d = int(input("d:"))
    f = int(input("f:"))
    g = int(input("g:"))
    y = ymani(l,m)+ymani(c,d)+ymani(f,g)
    if x == "x":
        break
    else:
        print("х өрнегінің мәні:",y)
        continue
print("Программа аяқталды!")"""
#6
"""def minimum(a,b):
    return (min(2*a,b+a)+min((2*a)-b,b))
while True:
    x = input("Программаны тоқтату үшін x жаз:")
    c = int(input("a:"))
    f = int(input("b:"))
    m = minimum(c,f)
    if x == "x":
        break
    else:
        print("х өрнегінің мәні:",m)
        continue
print("Программа аяқталды!")"""
#7
"""from math import sqrt
def fuu(a,b):
    return ((sqrt(a)+b)/(sqrt(b)+a))
while True:
    y = input("Программаны тоқтату үшін y жаз:")
    l = int(input("a:"))
    m = int(input("b:"))
    c = int(input("c:"))
    d = int(input("d:"))
    f = int(input("f:"))
    g = int(input("g:"))
    x = fuu(l,m)+fuu(c,d)+fuu(f,g)
    if y == "y":
        break
    else:
        print("х өрнегінің мәні:",x)
        continue
print("Программа аяқталды!")"""
#8
"""from math import sqrt
from math import pow
def medi(a,b,c):
    f = 0.5* (sqrt((2*pow(b,2))+(2*pow(c,2))-(pow(a,2))))
    return f
while True:
    y = input("Программаны тоқтату үшін y жаз:")
    d = int(input("a:"))
    h = int(input("b:"))
    j = int(input("c:"))
    ar = medi(d,h,j)
    if y == "y":
        break
    else:
        print("f өрнегінің мәні:", ar)
        continue
print("Программа аяқталды!")"""
#9
"""def sing(a):
    if a < 0:
        return -1
    elif a == 0:
        return 0
    else:
        return 1

def esepteu(x, y):
    z = sing(x) + sing(y)
    return z

while True:
    c = input("Программаны тоқтату үшін c жаз:")
    x = int(input("x:"))
    y = int(input("y:"))
    m = esepteu(x, y)
    if c == "c":
        break
    else:
        print("х өрнегінің мәні:",m)
        continue
print("Программа аяқталды!")"""
#10
"""from math import sqrt

def calculator_perimeter(a, b, h):
    perimeter = a + b + 2 * sqrt(h**2 + ((b - a) / 2)**2)
    return perimeter
while True:
    c = input("Программаны тоқтату үшін c жаз:")
    f = int(input("a:"))
    y = int(input("b:"))
    k = int(input("h:"))
    r = calculator_perimeter(f, y, k)
    if c == "c":
        break
    else:
        print("периметрлерінің қосындысы:",r)
        continue
print("Программа аяқталды!")"""
#11
"""import math
def distance(x1, y1, x2, y2):
    distance1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance1

def calculate_perimeter(x1, y1, x2, y2, x3, y3):
    AB = distance(x1, y1, x2, y2)
    BC = distance(x2, y2, x3, y3)
    CA = distance(x3, y3, x1, y1)

    perimeter = AB + BC + CA
    return perimeter
while True:
    c = input("Программаны тоқтату үшін c жаз:")
    x1, y1 = int(input("x1:")), int(input("y1:"))
    x2, y2 = int(input("x2:")), int(input("y2:"))
    x3, y3 = int(input("x3:")), int(input("y3:"))
    r = calculate_perimeter(x1, y1, x2, y2, x3, y3)
    if c == "c":
        break
    else:
        print("периметрі:",r)
        continue
print("Программа аяқталды!")"""
#12
"""def calculator(x_coords, y_coords):
    n = len(x_coords)
    a= 0.5 * abs(sum(x_coords[i] * (y_coords[(i+1)%n] - y_coords[(i+2)%n]) for i in range(n)))
    return a
while True:
    c = input("Программаны тоқтату үшін c жаз:")
    x = [0, 4, 6, 4, 0]
    y = [0, 0, 3, 6, 6]
    p = calculator(x, y)
    if c == "c":
        break
    else:
        print("Бесбұрыштің ауданы:", p)
        continue
print("Программа аяқталды!")"""
#13
"""def max_san(sandar):
    maximum = max(sandar)
    return maximum
while True:
    c = input("Программаны тоқтату үшін c жаз:")
    x = int(input("x:"))
    y = int(input("y:"))
    h = int(input("h:"))
    j = int(input("j:"))
    q = int(input("q:"))
    w = int(input("w:"))
    e = int(input("e:"))
    r = int(input("r:"))
    sandar = [x, y, h, j, q, w, e, r]
    max_num = max_san(sandar)
    if c == "c":
        break
    else:
        print("Ең үлкен сан:", max_num)
        continue
print("Программа аяқталды!")"""
#14
def arithmetic(num1, num2, tanba):
    if tanba == '+':
        return num1 + num2
    elif tanba == '-':
        return num1 - num2
    elif tanba == '*':
        return num1 * num2
    elif tanba == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "нөлге бөлу мүмкін емес"
    else:
        return "Белгісіз операция"

while True:
    x = input("программа тоқтау үшін х жаз:")
    if x == "x":
        break
    else:
        # Тесттер
        print(arithmetic(5, 3, '+'))  # 5 + 3 = 8
        print(arithmetic(10, 4, '-'))  # 10 - 4 = 6
        print(arithmetic(6, 2, '*'))  # 6 * 2 = 12
        print(arithmetic(8, 2, '/'))  # 8 / 2 = 4
        print(arithmetic(7, 0, '/'))  # Бөлу мүмкін емес
        print(arithmetic(4, 9, '%'))  # Белгісіз операция
        continue
print("Программа аяқталды!")



