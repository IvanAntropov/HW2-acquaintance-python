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

def Summ (n: float):
    num = n
    while num < 1:
        num = num *10
    print(num)
    nInInt = int(num)
    print(nInInt)
    print(n%1000)

number = InputValues('Enter real number: ')
print(f'{Summ(number)}')
