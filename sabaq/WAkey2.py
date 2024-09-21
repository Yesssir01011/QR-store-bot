#1
"""import numpy as np
a = [1, 3, 10.1, 6]
b = np.array(a, float)
print(b)"""
from typing import Any

from numpy import ndarray, dtype, floating, float_
from numpy._typing import _64Bit

#2
"""import numpy as np
m = np.arange(2, 11).reshape(3, 3)
print(m)"""
#3
"""import numpy as np
# 10 өлшемді нөлдік вектор
v = np.zeros(10)
print("Нөлдік вектор:", v)
# 5-ші элементті 7-ге ауыстыру
v[4] = 7
print("Ауыстырылған вектор:", v)
# Алтыншы мәнді 11-ге дейін жаңарту
v[5:11] = 0
print("Жаңартылған вектор:", v)"""
#5
"""import numpy as np
# Бастапқы массив
m1 = np.arange(10, 22)
print("Бастапқы массив:")
print(m1)
# Кері массив
m2 = m1[::-1]
print("Кері массив:")
print(m2)"""
#6
"""import numpy as np
# Берілген массив
a = [1, 2, 3, 4]
# NumPy массивіне айналдыру
b = np.array(a)
print("Нәтиже:", b)"""
#7
"""import numpy as np
# Матрицаның өлшемін енгізу
n = int(input("Матрицаның өлшемін енгізіңіз: "))
# Бастапқы матрица (барлық элементтері 1)
a = np.ones((n, n))
# Шекара орнату
a[1:-1, 1:-1] = 0
print("Бастапқы массив:")
print(a)"""
#8
"""import numpy as np
# Матрицаның өлшемін енгізу
n = int(input("Матрицаның өлшемін енгізіңіз: "))
# Бастапқы массив (барлық элементтері 1)
b = np.ones((n, n))
# Жаңа массив құру
a = 5
d = np.pad(b, a - 1, mode='constant', constant_values=a)
print("Нәтиже:")
print(d)"""
#9
"""import numpy as np
# Өлшемді енгізу
n = int(input("Шахмат тақтасының өлшемін енгізіңіз: "))
# Жаңа матрицаны құру
t = np.zeros((n, n), dtype=int)
# Жаңа матрицаны толтыру
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 1:
             t[i, j] = 1
print("Шахмат тақтасының үлгісі:")
print(t)"""
#10
"""import numpy as np
#Тізімді массивке айналдыру
# Бастапқы тізім
tizim = [1, 2, 3, 4, 5]
# Тізімді NumPy массивіне айналдыру
massiv1 = np.array(tizim)
# Массив түрін шығару
print("Бастапқы тізімдің түрі:", type(tizim))
print("NumPy массивінің түрі:", type(massiv1))
#Кортежді массивке айналдыру
kortej = (1, 2, 3, 4, 5)
# Кортежді NumPy массивіне айналдыру
massiv2 = np.array(kortej)
# Массив түрін шығару
print("Бастапқы кортеждің түрі:", type(kortej))
print("NumPy массивінің түрі:", type(massiv2))"""
#11
"""import numpy as np
# Бастапқы массив
massiv1 = np.array([10, 20, 30])
# Мәндерді кіру
man = input("Мәндерді енгізіңіз (көмегімен бөліп тізімді жазыңыз): ")
# Мәндерді тізімге айналдыру
a = [int(x) for x in man.split()]
# Массивға мәндерді қосу
massiv2 = np.append(massiv1, a)
print("Массивтің соңына мәндер қосқаннан кейін:")
print(massiv2)"""
#14
"""import numpy as np
#Формуласы F=(C×(9/5))+32
# Цельсий мәндерін массив ретінде беру
selci = np.array([0, 10, 20, 30, 40])
# Цельсий мәндерін Фаренгейтке түрлендіру
frangeit = selci * 9 / 5 + 32
print("Цельсий мәндері:", selci)
print("Фаренгейт мәндері:", frangeit)"""
#15
"""import numpy as np
# Array1 және Array2 мәндерін енгізу
Array1 = np.array([0, 10, 20, 40, 60])
Array2 = np.array([0, 40])
# Array1 элементтерінің Array2 элементтерімен салыстыру
salystyru = np.isin(Array1, Array2)
print("Array1 және Array2 элементтерінің әрқайсысын салыстырыңыз:")
print(salystyru)"""
#18
"""import numpy as np
# Array1 және Array2 мәндерін енгізу
Array1 = np.array([0, 10, 20, 40, 60])
Array2 = np.array([10, 30, 40])
# Екі массив арасындағы бірдей мәндерді табу
j = np.intersect1d(Array1, Array2)
print("Екі массив арасындағы жалпы мәндер:")
print(j)"""
#19
"""import numpy as np
# Берілген массив
m = np.array([10, 10, 20, 20, 30, 30])
# Массивтың бірегей элементтерін табу
birdei = np.unique(m)
print("Жоғарыда көрсетілген массивтің бірегей элементтері:")
print(birdei)"""
#20
"""import numpy as np
# Array1 және Array2 мәндерін енгізу
Array1 = np.array([0, 10, 20, 40, 60, 80])
Array2 = np.array([10, 30, 40, 50, 70, 90])
# Екі массив арасындағы айырмашылықты табу
aiyrmashylyq = np.setdiff1d(Array1, Array2)
print("Екі массив арасындағы айырмашылық:")
print(aiyrmashylyq)"""
#21
"""import numpy as np
a = np.array([[2,-1,1],
     [4,-5,2] ,
     [5,-7,3]])
d = np.linalg.det(a)
print("aнықтауыш:",int(d))
k = np.linalg.inv(a)
print("k:",k)
print("Кері матрица:",np.array(k,int))
b = np.dot(a,k)
print("Бірлік матрица:",b)
print("Бүтін сандармен:",np.array(b,int))"""
#22
"""import numpy as np
a = [[-1,1],
     [0,1]]

b = [[2,0],
     [-1,3]]

c = np.linalg.inv(a)
print("Кері матрица(A**-1):",c)

s = np.dot(c,a)
print("бірлік матрица(A**-1*A):",s)

x = np.dot(c,b)
print("x мәні(A**-1*B):",x)

g = np.dot(a,x)
print(f'A: {a} * X: {x} = B: {b} => {g} ={b}')"""
#B
import numpy as np
a = np.array([[-1,1],
     [0,2]],float)

b = np.array([[-1,0.5],
     [0,0.5]],float)

c = np.array([[1,2],
     [-2,4]],float)

if np.linalg.det(a) != 0:
    print("A детерминанты:",np.linalg.det(a))
    #A**-1*A*X*B=A**-1*C
    keri_a = np.linalg.inv(a)
    print("A кері матрицасы:",keri_a)
    #A**-1*A
    birlik_a = np.dot(keri_a,a)
    print("A-ның бірлік матрицасы:",birlik_a)
if np.linalg.det(b) != 0:
    print("B детерминанты:", np.linalg.det(b))
    #1*X*B**-1=A**-1*C*B**-1
    keri_b = np.linalg.inv(b)
    print("B кері матрицасы:",keri_b)
    #B*B**-1
    birlik_b = np.dot(keri_b,b)
    print("B-ның бірлік матрицасы:",birlik_b)
if np.linalg.det(c) != 0:
    print("C детерминанты:", np.linalg.det(c))
    #X = A**-1*C*B-1
    x = np.dot(keri_a,c,keri_b)
    print("Х-тің мәні болады:",x)
    bas = np.dot(a,x,b)
    print("Бастапқы мәні:",bas)
#23
"""
import numpy as np
a = [[1,1,-1],
     [3,7,-2],
     [3,1,-1]]
b = [[2],
     [-16],
     [2]]

c = np.linalg.inv(a)
print(np.dot(a,c))"""




