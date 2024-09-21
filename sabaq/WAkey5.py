#1
"""dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
print("dictionary_1:",dictionary_1)
print("dictionary_2:",dictionary_2)
dictionary_1.update(dictionary_2)
print("Біріктірілгеннен кейін:",dictionary_1)"""
#2
"""d = {'a': 10, 'b': 20, 'c': 30}
summa = sum(d.values())
print("Барлығының көбейтілген мәні:", summa)"""
#3
"""import math
sinus = {i: math.sin(i) for i in range(1, 11)}
print(sinus)"""
#4
"""keys = ['a', 'b', 'c']
values = [100, 200, 300]
sozdik = {keys[i]: values[i] for i in range(len(keys))}
print(sozdik)"""
#5
"""my = 'Pythonist'
d = []
for i in my:
    o = my.count(i)
    d.append(o)
    a = dict(list(zip(my,d)))
print(a)"""
#6
"""def to_dict(lst):
    return {item[0]: item[1] for item in lst}
a = [('a', 1), ('b', 2), ('c', 3)]
print(to_dict(a))
b = [('x', 'apple'), ('y', 'banana'), ('z', 'cherry')]
print(to_dict(b))"""
#7
"""def count_it(sequence):
    counts = {}
    for num in sequence:
        counts[num] = counts.get(num, 0) + 1
    return counts

sequence = [0, 1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = count_it(sequence)
print(result)"""
#8
"""my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
new_dict = {k: v for k, v in my_dict.items() if v >= 5}
new_dict['e'], new_dict['a'] = new_dict['a'], new_dict['e']
del new_dict['b']
new_dict['new_key'] = 'new_value'
print(new_dict)"""
#9
"""def max_dct(*dicts):
    new_dict = {}
    for dct in dicts:
        for key, value in dct.items():
            if key in new_dict:
                new_dict[key] = max(new_dict[key], value)
            else:
                new_dict[key] = value
    return new_dict

def sum_dct(*dicts):
    new_dict = {}
    for dct in dicts:
        for key, value in dct.items():
            new_dict[key] = new_dict.get(key, 0) + value
    return new_dict

# Демо сынақтар
dict1 = {'a': 5, 'b': 2, 'c': 3}
dict2 = {'a': 9, 'b': 4, 'd': 1}
dict3 = {'b': 7, 'c': 8, 'e': 6}

print("max_dct функциясынан кейін:")
print(max_dct(dict1, dict2, dict3)) 

print("\nsum_dct функциясынан кейін:")
print(sum_dct(dict1, dict2, dict3))"""
#1
"""D = {'1': 0, 2: 0, '3': 0}
print(D)"""
#2
"""adam = {'аты': 'Жандос', 'жасы': 25, 'жынысы': 'ер'}
print(adam)"""
#3
"""D = {'1': 1.29, '2': 0.43}
result = D['1'] * D['2']
D['result'] = result
print("Жаңа элементтің мәні:", result)
print("Жаңа сөздік:", D)"""
#4
"""D = {1: 1, '2': 2, '3': 3, 4: 4}
keys = list(D.keys())
values = list(D.values())
items = list(D.items())
print("Кілттер тізімі:", keys)
print("Мәндер тізімі:", values)
print("Элементтер тізімі:", items)"""
#5
"""D_1 = {'1': 1, '2': 2}
D_2 = {'2': 'two', '3': 3}
D_1.update(D_2)
num_elements = len(D_1)
values = list(D_1.values())
print("D_1 сөздігінің элементтерінің саны:", num_elements)
print("Сөздік элементтерінің мәндері:", values)"""
#6
"""D = {'a': 1, 'b': 2, 'c': 3}
del D['a']
del D['c']
print("Жойылған элементтерден кейін:", D)
D = {'a': 1, 'b': 2, 'c': 3}"""
#7
"""my_dict = {
    'бүтін сан форматындағы жол кілті бар элемент': 123,
    'нақты Сан форматындағы жол кілті бар элемент': 3.14,
    'кірістірілген сөздік форматындағы жол кілті бар элемент': {'а': 1, 'б': 2, 'с': 3},
    'кірістірілген сөздік түріндегі мән': {'кірістірілген сөздік түріндегі мән': 'орналастыратын кірістірілген сөздік түріндегі мән'},
    'бос тізім форматындағы жол кілті бар элемент': [],
    'жол кілті бар элемент': ('бір элементі бар кортеж пішімінде',),
    'Ok!': 'Ok!'
}
print(my_dict['Ok!'])"""
#8
"""days = ['Дүйсенбі', 'Сейсенбі', 'Ср', 'СС', 'жұма', 'сенбі', 'күн']
dictionary = {'D1': {}, 'd2': {}}
for index, day in enumerate(days):
    dictionary['D1'][index] = day
    dictionary['d2'][index] = day
mid_index = len(days) // 2
mid_element_D1 = dictionary['D1'][mid_index]
mid_element_d2 = dictionary['d2'][mid_index]
print(f"Кілт: мән форматында ортаға сәйкес келетін сөздік элементі: {'D1': {mid_index}: '{mid_element_D1}', 'd2': {mid_index}: '{mid_element_d2}'}")"""
#9
"""my_dict = {1: 'Бір', 2: 'Екі', 3: 'үш', 100: 'жүз'}
keys_sum = sum(my_dict.keys())
max_key = max(my_dict.keys())
min_key = min(my_dict.keys())
num_keys = len(my_dict.keys())
print("Кілттердің қосындысы:", keys_sum)
print("Кілттердің максималды мәні:", max_key)
print("Кілттердің минималды мәні:", min_key)
print("Кілттердің саны:", num_keys)"""
#10
"""my_dict = {'Pi': 3.14, 'e': 2.71, 'fi': 1.62}
filtered_values = [value for value in my_dict.values() if value > 2.5]
print("2.5 санынан асатын тұрақты мәндер:", filtered_values)"""
#11
"""D = {1: '1', 2: '2', 3: '3', 4: '4'}
D = {'1': 1, '2': 2, '3': 3, '4': 4}
print(D)"""
#12
"""D = {1: 1, '2': 2, '3': 3, 4: 4}
new_d = dict(D)
del D
print(new_d)"""
#13
"""goods = {
    "apple": {"name": "Алма", "cost": 25, "kg": 30},
    "pear": {"name": "алмұрт", "cost": 50, "kg": 5},
    "plum": {"name": "қара өрік", "cost": 55, "kg": 25},
    "шие": {"аты": "шие", "cost": 110, "kg": 15}
}

for key, value in goods.items():
    if value["cost"] >= 1000 and value["kg"] >= 10:
        print(value["name"])"""
                       #11 Labka
#1
"""a = [1.3, 2.5, 3.1]
b = [pow(x,2) for x in a]
print(b)"""
#2
"""odd_numbers = [x for x in range(10, 21) if x % 2 != 0]
print(odd_numbers)"""
#3
"""numbers_tuple = (3.27, 5.755, 7.321)
numbers_dict = {num: num / 10 for num in numbers_tuple}
print(numbers_dict)"""
#4
"""my_list = [1, 2, 3]
iterator = iter(my_list)
next_element = next(iterator)
print(next_element)"""
#5
"""class RangeIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            result = self.current
            self.current += 1
            return result

# Генераторды құру
class RangeIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return RangeIterator(self.start, self.end)

# Итераторды жасау
iterator = iter(RangeIterable(1, 20))

# __next__ әдісін қолдану арқылы алғашқы үш санды шығару
for _ in range(3):
    print(next(iterator))"""
#6
"""def gen_func(n):
    for i in range(1, n + 1):
        yield i
gen = gen_func(20)
for _ in range(3):
    print(next(gen))"""
#7
"""gen = (ord(char) for char in "генераторлар")
for code in gen:
    print(code)"""
#8
"""my_list = [(1, 2), (3+4), (5,), (6+7, 8), (9+10,)]
filtered_list = [item for item in my_list if isinstance(item, tuple) and len(item) > 1]
print(filtered_list)"""
#9
"""from collections.abc import Hashable
my_list = [3, 'ok', [1, 2], (True, False), {'flag': 1}]
filtered_list = [item for item in my_list if isinstance(item, Hashable)]
print(filtered_list)"""
#10
"""my_dict = {x: x**2 for x in range(20, 31)}
print(my_dict)"""
#11
"""def gen_fib(n: int) -> Generator[int, None, None]:
    # Фибоначчи сандарын қайтарады
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# gen_fib генераторын шақыру
fib_sequence = gen_fib(10)

# 10-шы Фибоначчи санын шығару
print(next(fib_sequence))

# Тізбектің алғашқы 10 санының қосындысын шығару
for _ in range(10):
    print(next(fib_sequence))"""









