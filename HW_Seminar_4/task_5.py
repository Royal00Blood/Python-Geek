#Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

f1 = open("text1.txt")
f2 = open("text2.txt")
text1 = f1.read()
text2 = f2.read()
f1.close()
f2.close()

list_numbers_1 = []
list_numbers_2 = []

def get_numbers(text):
    numbers = []
    number = 0
    for i in range(len(text)):
        if text[i+1]=='*' or text[i+1]=='=':
            while(text[i]!= '+' and text[i]!= '-' and text[i]!= '/'):
                k=0
                number += 10**k * int(text[i-k])
                k+=1
            numbers.append(number)
            number = 0
    return numbers
print(get_numbers(text1))