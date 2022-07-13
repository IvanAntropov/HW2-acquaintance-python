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

def Summ (number):
    suma = 0
    if number<0:
        number*=-1
    helpNumber = str(number)
    helpNumber = helpNumber.replace('.','')
    number = int(helpNumber)
    while number > 0:
        digit = number % 10
        suma = suma + digit
        number = number // 10
    return suma

number = InputValues('Enter real number: ')
print(f'{Summ(number)}')
