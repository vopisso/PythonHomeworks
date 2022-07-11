# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


x = (input('Input x-coordinate -> '))
y = (input('Input y-coordinate -> '))

def define_a_quarter(x, y):

    try:
        x = int(x)
    except:
        return 'Incorrect input: enter an integer'
    try:
        y = int(y)
    except:
        return 'Incorrect input: enter an integer'
    if(x > 0 and y > 0):
        return f'x = {x}; y = {y} -> 1'
    elif(x < 0 and y > 0):
        return f'x = {x}; y = {y} -> 2'
    elif(x < 0 and y < 0):
        return f'x = {x}; y = {y} -> 3'
    elif(x > 0 and y < 0):
        return f'x = {x}; y = {y} -> 4'
    else:
        return 'By the condition of the task, X is not equal to 0 and Y is not equal to 0'

print(define_a_quarter(x, y))