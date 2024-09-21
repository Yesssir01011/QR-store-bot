"""1) Компоненттері нақты сандар болып табылатын f файлы берілген.
Олардың қосындысын тауып жаңа файлға жазыңыз."""

"""with open('f.txt', 'r') as f:
    sandar = [int(line.strip()) for line in f]
print(sandar)
qosyndysy = sum(sandar)
print(qosyndysy)
with open('answer.txt', 'w') as a:
    a.write(str(qosyndysy))"""

"""23) f файлы берілген, оның компоненттері бүтін сандар. Файл компонентінің 
ешқайсысы нөлге тең емес. f файлында оң сандар мен теріс сандардың саны 
бірдей. Көмекші-h файлы арқылы, f файлының компоненттерін g файлына бір 
оң, бір теріс сан болатындай қайта жазыңыз."""

"""with open('f.txt', 'r') as f:
    sandar = [int(line.strip()) for line in f.readlines()]

with open('h.txt', 'r') as h:
    hsan = [int(line.strip()) for line in h.readlines()]

on = sorted([num for num in hsan if num > 0])
teris = sorted([num for num in hsan if num < 0])

with open('answer.txt', 'w') as a:
    for i in range(len(f)):
        if f[i] > 0:
            a.write(str(on))
        else:
            a.write(str(teris))"""

















#1
# Мәннің ұзындығын қайтаратын Функция:
"""def myFunc(e):
 return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)

#2
def myFunc(e):
 return e['year']
cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
print(cars)
#Жолдық мән
sorted(reverse=True|False, key=myFunc)
my_sentence = "Jessica found a dollar on the ground"
print("Original sentence: ", my_sentence)
# Сұрыпталған сөздер тізімін шығару:
print(sorted(my_sentence.split(), key=len))
#Кортеж
band_students = [
    ('Danny', 17, 'Trombone'),
    ('Mary', 14, 'Flute'),
    ('Josh', 15, 'Percussion')
]
print(sorted(band_students, key=lambda student: student[1]))
#Кері ретпен сұрыптау
band_students = [
    ('Danny', 17, 'Trombone'),
    ('Mary', 14, 'Flute'),
    ('Josh', 15, 'Percussion')
]
print(sorted(band_students, key=lambda student: student[2], reverse=True))


import timeit
code_to_test = ""
def bubble_sort(nums):
    # swapped True, цикл 1 рет орындалуы үшін
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
            # Элементтерді ауыстыру
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # swapped True келесі итерация үшін
            swapped = True

random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
elapsed_time = timeit.timeit(code_to_test, number=100)/10
print(elapsed_time)"""


















