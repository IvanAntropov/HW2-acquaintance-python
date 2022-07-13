# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

def InputValues (text: str):
    check = False
    while not check:
        try:
            number = int(input(f'{text}'))
            check = True
        except ValueError:
            number = int(input(f'{text}'))
    return number

def makeTheList(num):
    helpN = -num
    listOfNumbers = []
    while helpN != num + 1:
        listOfNumbers.append(helpN)
        helpN+=1
    return listOfNumbers 

# def multiOfElements(listN):
 

numberN = InputValues('Enter number N: ')
position = input('Enter position: ')
position.split(' ')
print(type(position))
print (makeTheList(numberN))
# print(multiOfElements(makeTheList(numberN)))