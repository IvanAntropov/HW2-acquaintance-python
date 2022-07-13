# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


def InputValues (text: str):
    check = False
    while not check:
        try:
            number = float(input(f'{text}'))
            check = True
        except ValueError:
            number = float(input(f'{text}'))
    return number

def Summ (n):
    num = n
    result = 0
    while num is not int:
        num = num * 10
        print (num)
    return result

number = InputValues('Enter real number: ')
print(f'{Summ(number)}')

# n = int(input())
 
# suma = 0
# mult = 1
 
# while n > 0:
#     digit = n % 10
#     suma = suma + digit
#     mult = mult * digit
#     n = n // 10
 
# print(suma)
# print(mult)
