"""
Допрацюйте гру з заняття наступним чином:

- додайте підказки для користувача:
    - якщо різниця між числами 1-2 - "Гарячо"
    - якщо різниця між числами 3-5 - "Тепло"
    - якщо різниця між числами 6 і більше - "Холодно"

- додайте лічильник спроб вгадати. користувач повинен вгадати число за фіксовану кількість спроб,
  якщо він не вгадав за фіксовану кількість спроб - гра завершується з відповідним повідомленням.
"""

from random import randint


def get_user_number(prompt, lower_limit=None, upper_limit=None):
    while True:
        try:
            res = int(input(f'{prompt} (ціле число): '))
        except Exception:
            print('Ви ввели невірний вид даних!')
        else:
            if lower_limit is not None:
                if res < lower_limit:
                    print(f'Число має бути більше за {lower_limit}!')
                    continue
            if upper_limit is not None:
                if res > upper_limit:
                    print(f'Число має бути менше за {upper_limit}!')
                    continue
            return res


def get_comp_number(lower_limit, upper_limit):
    comp_number = randint(lower_limit, upper_limit)
    return comp_number


def compare_numbers(comp_number, user_number):
    comparing_numbers = comp_number - user_number
    if -2 <= comparing_numbers <= 2:
        print('Гарячо')
    elif -5 <= comparing_numbers <= 5:
        print('Тепло')
    else:
        print('Холодно')


def game_guess_number():
    lower_limit = 0
    upper_limit = 10

    comp_number = get_comp_number(lower_limit, upper_limit)

    counter = 0
    while True:
        counter += 1
        user_number = get_user_number(f'Вгадайте число [{lower_limit}-{upper_limit}]', lower_limit, upper_limit)

        if user_number == comp_number:
            print('Ви вгадали число!')
            break
        elif counter == 3:
            print('Ви використали всі спроби')
            break

        compare_numbers(comp_number, user_number)


game_guess_number()
