"""
Дана довільна строка.
Напишіть код, який знайде в ній і виведе на екран кількість слів,
які містять дві голосні літери підряд.
"""

userinput = input('Enter a sentence: ')

vowels = 'euioa'
counter = 0

words = userinput.split()

for word in words:
    next_vowel = 0
    for letter in word:
        if letter in vowels:
            next_vowel += 1
            if next_vowel == 2:
                counter += 1
                break
print(f'There\'re {counter} words with 2 vowels.')


"""
Є два довільних числа які відповідають за мінімальну і максимальну ціну.
Є Dict з назвами магазинів і цінами: 
{ "cito": 47.999,
"BB_studio" 42.999,
"momo": 49.999,
"main-service": 37.245,
"buy.now": 38.324,
"x-store": 37.166,
"the_partner": 38.988,
"store": 37.720,
"rozetka": 38.003 }.
Напишіть код, який знайде і виведе на екран назви магазинів,
ціни яких попадають в діапазон між мінімальною і максимальною ціною.
"""

dct = {
    'cito': 47.999,
    "BB_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.now": 38.324,
    "x-store": 37.166,
    "the_partner": 38.988,
    "store": 37.720,
    "rozetka": 38.003
}

lower_limit = 37.166
upper_limit = 49.999

for item in dct.items():
    key = item[0]
    value = item[1]
    if lower_limit <= value:
        if upper_limit >= value:
            print(item)