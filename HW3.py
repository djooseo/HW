# Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові.
# Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'".
# Слово та номер символу отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".

while True:
    number = input('Enter \'5\': ')
    word = input('Enter \'Dimension\': ')
    if number == '5' and word == 'Dimension':
        print('The {} symbol in {} is \'{}\''.format(number, word, word[4]))
        break
    else:
        continue


# Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.

userinput = input('Enter a sentence: ')
result = userinput.split()
print(len(result))


# Існує ліст з різними даними,
# наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2),
# який би містив всі числові змінні (int, float), які є в lst1.

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for num in lst1:
    if type(num) in (int, float):
        lst2.append(num)
print(lst2)
