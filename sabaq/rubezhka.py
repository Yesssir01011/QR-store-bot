#1)
"""text = "Алматы әсем қала.Және Еліміздің екінші Астанасы деп те аталады."
birinshi_nukte = text.index(".")
ekinshi_nukte = len(text)
sany = 0
basy_index = min(birinshi_nukte, ekinshi_nukte)
sony_index = max(birinshi_nukte, ekinshi_nukte)
for i in range(basy_index , sony_index):
    if text[i] == 'а' or text[i] == 'А':
        sany += 1
print("Ішкі жолдағы 'а' әріптерінің саны:", sany)"""
#2)
"""sandar = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10)
count_dict = {}
for san in sandar:
    if san in count_dict:
        count_dict[san] += 1
    else:
        count_dict[san] = 1

for key, value in count_dict.items():
    if value == 1:
        print("Ұқсас сандардың саны:",key)"""
#3)
"""def generate_random_tuple(n):
    import random
    random_numbers = [random.randint(-100, 30) for _ in range(n)]
    max_index = -1
    max_value = float('-inf')
 
    for i, num in enumerate(random_numbers):
        if num > max_value:
            max_value = num
            max_index = i

    if max_index == -1:
        return tuple()

    return tuple(random_numbers[max_index + 1:])


# N элементті тізім
n = 10

# Кортежді жасау
result_tuple = generate_random_tuple(n)

print("Жасалған кортеж:", result_tuple)"""
decimal_number = 10
binary_number = bin(decimal_number)
binary_equivalent = binary_number[2:]
print("10-дық санау жүйесінен 2-лік санау жүйесіне айналдырылған:", binary_equivalent)