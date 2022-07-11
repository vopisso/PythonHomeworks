# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


day = input('Enter the number of the day of the week -> ')

def is_weekend(num):

    try:
        num = int(num)
    except:
        return 'Incorrect input: enter an integer'
    if(num < 1 or num > 7):
        return 'Incorrect input: enter the number from 1 to 7'
    elif(num == 6 or num == 7):
        return f'- {num} -> YES'
    else:
        return f'- {num} -> NO'

print(is_weekend(day))