# На колесе рулетки карманы пронумерованы от 0 до 36.
# Ниже приведены цвета карманов:
# карман 0 зеленый;
# для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет,
# карманы с четным номером – черный;
# для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет,
# карманы с четным номером – красный;
# для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет,
# карманы с четным номером – черный;
# для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет,
# карманы с четным номером – красный. Напишите программу,
# которая считывает номер кармана и показывает, является ли этот карман зеленым,
# красным или черным. Программа должна вывести сообщение об ошибке,
# если пользователь вводит число, которое лежит вне диапазона от 0 до 36.
# Формат входных данных
# На вход программе подаётся одно целое число.
#
# Формат выходных данных
# Программа должна вывести цвет кармана либо сообщение «ошибка ввода»,
# если введённое число лежит вне диапазона от 0 до 36.


def result(num):
    if num == 0:
        print("Green")
    if (1 <= num and num <= 10) or (19 <= num and num <= 28):
        if num % 2 == 0:
            print('Black')
        else:
            print('Red')
    if (11 <= num and num <= 18) or (29 <= num and num <= 36):
        if num % 2 == 0:
            print('Red')
        else:
            print('Black')

number = int(input('Введите целое число: '))
result(number)