# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
text_1 = input('Введите строку 1 ')
text_2 = input('Введите строку 2 ')
if len(text_1)>len(text_2):
    print(text_1.count(text_2))
else:
    print(text_2.count(text_1))

