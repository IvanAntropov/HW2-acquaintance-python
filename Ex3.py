# Задайте список из n чисел последовательности (1 + 1/n)^n. и выведите на экран их сумму.

def InputValues (text: str):
    check = False
    while not check:
        try:
            number = int(input(f'{text}'))
            check = True
        except ValueError:
            number = int(input(f'{text}'))
    return number

def orderOfNumbers(num):
    order = 0
    summ = 0
    listOfMulti = []
    for i in range(num):
        helpI = i+1
        order = (1 + 1/helpI)**helpI
        summ += order
        listOfMulti.append(f'{helpI}: {order}')
    defString = f'A set of order for {num} is {listOfMulti} and sum of numbers is {summ}'
    return defString

numberN = InputValues('Enter number N: ')
print(orderOfNumbers(numberN))