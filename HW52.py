"""
AI. Порграма має відповісти на питання чи є введений стрінг
1 - номером телефону
2 - email-ом
3 - Іменем з ініціалами
4 - Даними невідомого формату

+380631112233 -> Phone
bcdef@abc.efg -> Email   3+ letters @ 3 letters. 3 letters
Bill J.I. -> Name   2 words
something else -> unknown
"""

userinput = input('Enter your data: ')

split = userinput.split(' ')
email_split = userinput.split('@')
if len(split) == 2:
    _name = split[0]
    initials = split[1]
    if _name.isalpha() and _name.capitalize():
        if initials[-1] == '.' and initials[-3] == '.':
            if initials[0].isalpha() and initials[2].isalpha():
                if initials[0].upper() and initials[2].upper():
                    print('Name')
elif len(email_split) == 2:
    email_name = email_split[0]
    email_at = email_split[1]
    if email_name.isalnum() and email_name.islower():
        if email_at[-4] == '.' and email_at[:3].isalpha() and email_at[4:].isalpha():
            print('Email')
elif len(userinput) == 13:
    if userinput[1:].isdigit():
        if userinput[0] == '+':
            print('Phone number')
else:
    print('Not real data')