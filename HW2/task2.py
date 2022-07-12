# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = (input('Enter positive integer: '))

def factorial(num):

    try:
        num = int(num)
    except:
        return 'Incorrect input: enter positive INTEGER'
    
    if(num < 0):
        return 'Incorrect input: enter POSITIVE integer'
    else:
        result = 1
        str_result = '['
        for i in range(1, num + 1):
            result *= i
            if((i + 1) > num):
                str_result += str(result) + ']'
            else:
                str_result += (str(result) + ', ')
        return str_result

print(factorial(number))