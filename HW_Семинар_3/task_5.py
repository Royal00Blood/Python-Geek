# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#
# Пример:
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
count = int(input('введите номер элемента фибоначи : '))
def fibonachi_solve(n):
    fib1 = 1
    fib2 = 1
    if n>2:
        i = 0
        while i < n - 2:
            fib_sum = fib1 + fib2
            fib1 = fib2
            fib2 = fib_sum
            i = i + 1
    return fib2
def complit_list_fib(n):
    list_fib = []
    for i in range(n):
        list_fib.append(fibonachi_solve(n-i)*(-1)**(i+1))
    list_fib.append(0)
    for i in range(1,n+1):
        list_fib.append(fibonachi_solve(i))
    return list_fib
print(complit_list_fib(count))
