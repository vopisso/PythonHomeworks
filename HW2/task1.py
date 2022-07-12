# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Input number: ')

def sum_of_digits(num):
    sum = 0
    for i in num:
        if(i.isdigit()):
            sum += int(i)
    return f'{num} -> {sum}'

print(sum_of_digits(number))