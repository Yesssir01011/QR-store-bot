#1
"""text = "Almaty"
sany = 0
for i in text:
    if i.lower() == 'a':
        sany += 1
print("a әріпі",text,"сөзінде",sany,"рет кездеседі")"""
import re

#1 Функциямен
"""def arip_sany(text):
    sany = 0
    for i in text:
        if i.lower() == 'a':
            sany += 1
    return sany
text = input("text = ")
print("a әріпі",text,"сөзінде",arip_sany(text),"рет кездеседі")"""

#2
"""def birinshi_songy(text):
    birinshi = text[0]
    songy = text[-1]
    b = text[1:-1]
    a = songy + b + birinshi
    return a

text = "Берілген жолда бірінші және соңғы таңбаны ауыстырыңыз жолдар."
swapped_text = birinshi_songy(text)
print("Ауыстырылған жол:", swapped_text)"""

#3
"""def qosu(text):
    text = " " + text[1:]
    text = text[:-1] + "."
    return text

text = "Берілген жолда бірінші таңбаның орнына бос орын, ал соңғысына -нүкте қойыңыз."
modified_text = qosu(text)
print("Өңделген жол:", modified_text)"""

#4
"""def birinshi(text):
    return text[1:]

i = "Берілген жолда бірінші таңбаны жойыңыз."
modified_text = birinshi(i)
print("Өңделген жол:", modified_text)"""

#5
"""def qoss(text):
    return text + ""

input_text = "Берілген жолда жолдың соңына белгісін қосыңыз."
modified_text = qoss(input_text)
print("Өңделген жол:", modified_text)"""

#6
"""def count_digits(text):
    digit_count = 0
    for char in text:
        if char.isdigit():
            digit_count += 1
    return digit_count

input_text = "Берілген жолда цифрлар таңбаларының санын есептеңіз (\"0\" - ден \"9\" - ға дейін)."
digit_count = count_digits(input_text)
print("Цифрлар таңбаларының саны:", digit_count)"""

#7
"""def bar_joq(text):
    for char in text:
        if char.isdigit():
            return True
    return False

input_text = "Берілген жолда цифр таңбасы бар-жоғын анықтаңыз."
if bar_joq(input_text):
    print("Мәтінде цифр таңбасы бар.")
else:
    print("Мәтінде цифр таңбасы жоқ.")"""

#8
"""def aaa(text):
    return ''.join(['"' + char + '"' if char.isspace() else char for char in text])

input_text = "Берілген жолда әр бос орынның орнына "" белгісін қойыңыз."
modified_text = aaa(input_text)
print("Өңделген жол:", modified_text)"""

#9
"""def joiu(text):
    return text[:-1]

input_text = "Берілген жолда соңғы таңбаны жойыңыз."
modified_text = joiu(input_text)
print("Өңделген жол:", modified_text)"""

#10
"""text = "Astana qalasy Almatyga qaraganda ote suyq"
print("Дейін:",text)
bos_oryn = text.replace(" ","")
print("Кейін:",bos_oryn)"""
#Функция арқылы:
"""def bos_oryn_joiu(text):
    return text.replace(" ","")
text = input("Мәтін жаз:")
print("Дейін:",text)
print("Кейін:",bos_oryn_joiu(text))"""

#11
"""def ekinsh_tort(text):
    new_text = ""
    for index, char in enumerate(text):
        if index != 1 and index != 3:
            new_text += char
    return new_text

input_text = "Берілген жолда екінші және төртінші таңбаларды алып тастаңыз."
modified_text = ekinsh_tort(input_text)
print("Өңделген жол:", modified_text)"""

#12
"""def barlyq(text):
    return [ord(char) for char in text]

input_text = "Берілген жолдың барлық таңбаларының кодтарының қосындысын табыңыз."
character_codes = barlyq(input_text)
print("Барлық таңбалардың кодтары:", character_codes)"""

#13
"""def remove_first_word(text):
    # Мәтінні бос орындар бойынша бөліп аламыз
    words = text.split()
    # Егер мәтінде бірнеше сөз болса, бірінші сөзді алып тастаймыз
    if len(words) > 1:
        return ' '.join(words[1:])
    else:
        # Бір сөзден тұратын мәтіндер үшін қайтарады
        return ""

input_text = "Берілген жолдың бірінші сөзін жойңыз. Онда сөздерді бөлу бос орын арқыл ұйымдастрылған."
modified_text = remove_first_word(input_text)
print("Өңделген жол:", modified_text)"""

#14
"""text = ("Astana Qazaqstannyn astanasy, Jane de Almaty ekinshi astana bolyp sanalady.")
utir_sany = 0
nukte_sany = 0
for symbol in text:
    if symbol == ".":
        nukte_sany += 1
    if symbol == ",":
        utir_sany += 1
print("Нүктелердің саны:", nukte_sany)
print("Үтірлердің саны:", utir_sany)"""
#Функция арқылы:
"""def utir_nukte(text):
    utir_sany = 0
    nukte_sany = 0
    for symbol in text:
        if symbol == ".":
            nukte_sany += 1
        if symbol == ",":
            utir_sany += 1
    return utir_sany,nukte_sany
text = input("text:")
utir , nukte = utir_nukte(text)
print("Нүктелердің саны:", utir)
print("Үтірлердің саны:", nukte)"""

#15
"""def count_odd_and_square_numbers(text):
    # Мәтінні бос орындар бойынша бөліп аламыз
    words = text.split()
    odd_count = 0
    square_count = 0

    # Көрсеткілердің бөлшектерін тексереміз
    for word in words:
        # Сөздегі санды int түріне айналдырамыз
        try:
            number = int(word)
            # Санды тексереміз
            if number % 2 != 0:
                odd_count += 1
            if int(number ** 0.5) ** 2 == number:
                square_count += 1
        except ValueError:
            pass

    return odd_count, square_count


input_text = "Берілген жолдағыжай және квадрат жақшалардың санын есептеңіз."
odd_count, square_count = count_odd_and_square_numbers(input_text)
print("Жай сандардың саны:", odd_count)
print("Квадрат сандардың саны:", square_count)"""

#16
"""def convert_to_quotes(text):
    return '"' + text + '"'

input_text = "Берілген жолды тырнақшаға алыңыз."
quoted_text = convert_to_quotes(input_text)
print("Тырнақшаға алынған жол:", quoted_text)"""

#17
"""def add_underscores(text):
    text_length = len(text)
    if text_length >= 25:
        return text[:text_length - 25] + "_" * 25
    else:
        return "_" * (25 - text_length) + text

input_text = "Берілген жолдың соңына жолдың ұзындығын 25-ке жеткізіп, \" _ \" таңбаларын қосыңыз."
modified_text = add_underscores(input_text)
print("Өңделген жол:", modified_text)"""

#18
"""def find_least_common_letter(text):
    # Сөздерді бөліп алу
    words = text.split()
    # Әр сөздегі әріптердің санын есептеу
    letter_counts = {}
    for word in words:
        for char in word:
            if char.isalpha():
                char = char.lower()  # Кез-келген әріпті кішірейтін
                if char in letter_counts:
                    letter_counts[char] += 1
                else:
                    letter_counts[char] = 1
    # Ең кем дегенде бір рет кіретін әріпті табу
    least_common_letter = min(letter_counts, key=letter_counts.get)
    return least_common_letter

input_text = "Берілген жолда кем дегенде бір латын әріпі кіретінін анықтаңыз"
result = find_least_common_letter(input_text)
print("Кем дегенде бір рет кіретін әріп:", result)"""

#19
"""def find_first_star_index(text):
    index = text.find("*")
    return index

input_text = "Берілген жолда * таңбасының бірінші кездесу орнын табыңыз."
result = find_first_star_index(input_text)
print("Бірінші * таңбасының кездесу орны:", result)"""

#20
"""def remove_first_and_last_chars(text):
    if len(text) < 2:
        return ""
    else:
        return text[1:-1]

input_text = "Берілген жолда бірінші және соңғы таңбадан басқасының барлығын жойыңыз."
modified_text = remove_first_and_last_chars(input_text)
print("Өңделген жол:", modified_text)"""

#21
"""def find_next_punctuation(text):
    punctuation = ["!»", "?»", "!\"", "?\"", "! ", "? ", "!", "?", ".", ",", ";", ":", "'", '"']
    next_punctuation_indices = [text.find(p) for p in punctuation if text.find(p) != -1]
    if next_punctuation_indices:
        return min(next_punctuation_indices)
    else:
        return -1

input_text = "Берілген мәтіннен қай таңбалар (!», ?». немесе өзгерістерінен) қайсысының алдында кездесетінін анықтау үшін Python функциясын жасаңыз."
result = find_next_punctuation(input_text)
print("Келесі таңба кездесетінін орны:", result)"""

#22
"""def count_open_and_close_brackets(text):
    open_bracket_count = text.count('(')
    close_bracket_count = text.count(')')
    return open_bracket_count, close_bracket_count

input_text = "Берілген мәтінде ашылатын (және) жабылатын жай жақшалардың санын табу үшін Python функциясын жасаңыз."
open_count, close_count = count_open_and_close_brackets(input_text)
print("Ашылатын жақшалар саны:", open_count)
print("Жабылатын жақшалар саны:", close_count)"""

#23
"""def add_extra_period(text):
    # Мәтіндегі соңғы нүктені табу
    last_period_index = text.rfind('.')

    # Егер нүкте табылмаса немесе соңғы символ нүктен басқа болса, мәтінге басқа нүкте қосу
    if last_period_index == -1 or last_period_index == len(text) - 1:
        return text + '.'

    # Нүктенің кейінгі нүктен кейін қойылуы
    return text[:last_period_index + 1] + '.' + text[last_period_index + 1:]


input_text = "Берілген мәтінде әр нүктеден кейін тағы бір нүкте қойыңыз"
result = add_extra_period(input_text)
print("Өңделген мәтін:", result)"""

#24
"""def add_space_after_period(text):
    # Мәтіндегі барлық нүктелердің индексін табу
    period_indices = [i for i, char in enumerate(text) if char == '.']

    # Нүктелердің кейінгінде бос орын қосу
    for index in reversed(period_indices):
        text = text[:index + 1] + ' ' + text[index + 1:]

    return text


input_text = "Берілген мәтінде әр нүктеден кейін бос орын қойыңыз."
result = add_space_after_period(input_text)
print("Өңделген мәтін:", result)"""

#25
"""def replace_exclamation_with_space(text):
    return text.replace("!", " ")

input_text = "Жолдағы әрбір \"!\"таңбасын \"\" бос орынға ауыстырыңыз."
result = replace_exclamation_with_space(input_text)
print("Өңделген мәтін:", result)"""

#26
"""def find_empty_space(text):
    for index, char in enumerate(text):
        if char.isspace():
            return index
    return -1  # Бос орын кіретінің кезінде табылмады

input_text = "Берілген жолға бос орын кіретінін анықтаңыз."
empty_space_index = find_empty_space(input_text)
print("Бос орын кіретінің орны:", empty_space_index)"""

#27
"""def count_plus_minus(text):
    plus_count = text.count('+')
    minus_count = text.count('-')
    return plus_count, minus_count

input_text = "Берілген жолда \"- +\"таңбалар тіркесімдерінің санын есептеңіз."
plus, minus = count_plus_minus(input_text)
print("Тіркесімдерің саны:", plus, "тңба + және", minus, "тңба -")"""

#28
"""import re
text = "АLMАTY AСTANA"
latyn_text = re.findall(r'[a-zA-Z]', text)
print(latyn_text)

def latyn(text):
    return re.findall(r'[a-zA-Z]', text)
text = "АLMАTY AСTANA"
print(latyn(text))"""

#29
"""def collapse_spaces(text):
    return ' '.join(text.split())

input_text = "Берілген   жолда  қатарынан   бос   орындарды   бір   бос   орынға   ауыстырыңыз."
result = collapse_spaces(input_text)
print("Өңделген мәтін:", result)"""

#30
"""def count_words(text):
    # Бір немесе бірнеше бос орынға бөліп аламыз
    words = text.split()
    return len(words)

input_text = "Берілген жолдағы сөздердің санын санаңыз. Бөлгіш ретінде бір немесе бірнеше бос орын қарастырылады"
word_count = count_words(input_text)
print("Сөздердің саны:", word_count)"""

#31
"""def add_length_to_end(text):
    length = len(text)
    return text + " " + str(length)

input_text = "Жол берілген."
result = add_length_to_end(input_text)
print("Өңделген жол:", result)"""

#32
"""def add_exclamation_before_each_character(text):
    return "!".join(text)

input_text = "Берілген жолда әр таңбаның алдына ! символ қойыңыз."
result = add_exclamation_before_each_character(input_text)
print("Өңделген жол:", result)"""

#33
"""def merge_lists(list1, list2):
    # Жаңа жолдың жұп орындарында бірінші жолдың элементтері
    first_part = list1[:-1]
    # Тақ орындарда екінші жолдың элементтері
    second_part = list2[1:]
    # Жаңа жолды жасау
    new_list = first_part + second_part
    return new_list

# Берілген екі жол
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# Жаңа жол
new_list = merge_lists(list1, list2)
print("Жаңа жол:", new_list)"""

#34
"""text = ("Almaty asem qala")
print("Дейін:", text)
almastyru_text = text[::-1]
print("Кейін:",almastyru_text)"""
#Функция арқылы
"""def keri_jazu(text):
    return text[::-1]
text = input("Matin jazynyz:")
print("Дейін:", text)
print("Кейін:",keri_jazu(text))"""

#35
"""def increment_char_codes(text):
    # Мәтіннің барлық таңбаларын кодтарына өзгерту
    incremented_text = ''.join(chr(ord(char) + 1) for char in text)
    return incremented_text

input_text = "Берілген жолда барлық таңбаларды олардың кодтарының өсуіне сәйкес орналастырыңыз."
result = increment_char_codes(input_text)
print("Өңделген мәтін:", result)"""

