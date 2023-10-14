import time


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


def decorator_time(func):

    def time_function(*args, **kwargs):
        time_before_func = time.time()
        res = func(*args, **kwargs)
        time_after_func = time.time()
        timer = time_after_func - time_before_func
        print(f'Пройшло {timer} секунд.')

        return timer
    return time_function
