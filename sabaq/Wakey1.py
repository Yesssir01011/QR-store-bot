#1
"""from math import sqrt
def f(n):
    return (sqrt(n)+n)/2
x=f(5)+f(12)+f(19)
print(x)"""
#2
"""from  math import sin
def sinus(n):
    return (sin(n)+n)/3
y = sinus(1)+sinus(3)+sinus(5)
print(y)"""
#3
"""def maximum(a,b):
    return (max(a,2*b)+max((2*a)-b,b))
m = maximum(5,7)
print(m)"""
#4
"""from math import sqrt
def xmani(j):
    return (sqrt(j)+j)
x = (xmani(5)/xmani(7))+(xmani(12)/xmani(8))+(xmani(19)/xmani(2))
print(x)"""
#5
"""from math import sin
def ymani(a,b):
    return ((a+sin(a))/(sin(b)+b))
y = ymani(2,5)+ymani(6,3)+ymani(1,4)
print(y)"""
#6
"""def minimum(a,b):
    return (min(2*a,b+a)+min((2*a)-b,b))
m = minimum(5,7)
print(m)"""
#7
"""from math import sqrt
def fuu(a,b):
    return ((sqrt(a)+b)/(sqrt(b)+a))
x = fuu(8,15)+fuu(6,12)+fuu(7,21)
print(x)"""
#8
"""from math import sqrt
from math import pow
def medi(a,b,c):
    f = 0.5* (sqrt((2*pow(b,2))+(2*pow(c,2))-(pow(a,2))))
    return f
d = int(input("a:"))
h = int(input("b:"))
j = int(input("c:"))
a = medi(d,h,j)
print(a)"""
#9
def sing(a):
    if a < 0:
        return -1
    elif a == 0:
        return 0
    else:
        return 1

def calculate_z(x, y):
    z = sing(x) + sing(y)
    return z

x = -2
y = 3
result = calculate_z(x, y)
print(result)




