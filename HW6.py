"""
Напишіть функцію, що приймає один аргумент будь-якого
типу та повертає цей аргумент, перетворений на float.
Якщо перетворити не вдається функція має повернути 0.
"""


def turn_into_float(arg):
    try:
        res = float(arg)
        return res
    except Exception:
        return 0


arg_input = turn_into_float(arg=1)
print(arg_input)

"""
Напишіть функцію, що приймає два аргументи. Функція повинна:
- якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів
- якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
- у будь-якому іншому випадку повернути кортеж з цих аргументів
"""


def arg_processing(arg1, arg2):
    if type(arg1) in (int, float) and type(arg2) in (int, float):
        return arg1 * arg2
    elif type(arg1 and arg2) is str:
        return arg1 + arg2
    else:
        return arg1, arg2


func_res = arg_processing(arg1=10, arg2={20.55})
print(func_res)

"""
Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
Попросіть користувача ввести свій вік.

- якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
- якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це фільм для дорослих!"
- якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
- якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить!"
- у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"

Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік.
Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача
(1 - рік, 22 - роки, 35 - років і тд...).
"""


def age_input(prompt):
    try:
        res = int(input(f'{prompt}'))
        return res
    except Exception:
        print("Будь ласка введіть ваш реальний вік!")


def word_form(res):
    last_digit = res % 10
    age = 'рік' if last_digit == 1 and res != 11 else 'роки' if 1 < last_digit < 5 and (
            res < 10 or res > 20) else 'років'
    return age


def cashier_in_cinema(res):
    if '7' in str(res):
        print(f"Вам {res} {word_form(res)}, вам пощастить!")
    elif res < 7:
        print(f"Тобі ж {res} {word_form(res)}! Де твої батьки?")
    elif res < 16:
        print(f"Тобі лише {res} {word_form(res)}, а це фільм для дорослих!")
    elif res > 65:
        print(f"Вам {res} {word_form(res)}? Покажіть пенсійне посвідчення!")
    else:
        print(f"Незважаючи на те, що вам {res} {word_form(res)}, білетів всеодно нема!")
    return


def final_res():
    prompt = 'Вкажіть ваш вік: '
    res = age_input(prompt)
    cashier_in_cinema(res)


final_res()
