import array
from figures import Wakey_module

"""from random import randint as rnd
a = [rnd(5,100) for i in range(10)]
print(a)
f = Wakey_module.taq_sany(a)
g = Wakey_module.jup_qos(a)
print("Тақ сандардың саны:",f)
print("Жұп сандар қосындысы:",g)"""

"""a = array.array('i', [4,5,8,7,9,6,3,5,6,10])
c = a.tolist()
print(c)
b = 0
l = 0
for i in c:
    if i%2 == 1:
        b += 1
    if i%2 != 1:
        l+=i
f = b
print(f)
print(l)"""
"""a = array.array('i', [4,5,8,7,9,6,3,5,6,10])
c = a.tolist()
f = Wakey_module.taq_sany(c)
g = Wakey_module.jup_qos(c)
print("Тақ сандардың саны:",f)
print("Жұп сандар қосындысы:",g)"""

"""a = int(input("массив жасауш үшін 0 енгіз :"))
g = Wakey_module.kezdeisoq_massiv(a)
print(g)"""

#2
"""a = array.array("d",[12.1,5.6,4.3,9.4,8.9,2.7,1.6,2.1,5.8,7.1,2.4,6.5,8.7])
b = a.tolist()
g = len(b)//2
h = sum(b)/len(b)
print(h)
b.pop(g)
b.insert(int(g),float(h))
print(b)
print(g)"""

"""from figures import Wakey_module
a = array.array("d",[12.1,5.6,4.3,9.4,8.9,2.7,1.6,2.1,5.8,7.1,2.4,6.5,8.7])
a.pop(Wakey_module.indecs(a))
a.insert(Wakey_module.indecs(a),Wakey_module.arif_orta(a))
print(a)"""
#3
"""my_massiv = array.array("i",[42,56,8,7,9,6,3,5,6,10,57])
h = Wakey_module.arif_orta(my_massiv)
print(f'\t массивтің орташа мәні: {h}')
j = sum( 1 for x in my_massiv if x > h)
print(f'\t Абсолютті мәні үлкен сандардың саны: {j}')
for i in my_massiv:
    if i > h:
        f = my_massiv.index(i)
        print(f'\t Абсолютты мәні үлкен сандар индексі {i}: {f}')"""

#4
"""from array import array

# массив 10
input_array = array('i', [177, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Минималды және максималды элементтердің индекстерін табамыз
min_index = input_array.index(min(input_array))
max_index = input_array.index(max(input_array))

# Минималды және бірінші элементтерді ауыстырыңыз
input_array[min_index], input_array[0] = input_array[0], input_array[min_index]

# результаты
print("Массив ауысканнан кейын:")
print(input_array)"""
#5
"""from array import array
my_array = array('i', [5, 12, 8, 4, 19, 7, 10, 15, 3, 11, 6, 9, 18, 222, 14, 17, 1, 13, 16])
max_element = max(my_array)
min_element = min(my_array)
s = max_element + min_element
print(s)"""