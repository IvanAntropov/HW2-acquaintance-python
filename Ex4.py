# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

def InputValues(text: str):
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
        helpN += 1
    return listOfNumbers


def makeTextPositionAndMulti(listOfNumbers):
    
    position = input('Enter position: ') # я бы мог сделать проверку на дурака, но я много времени потратил чтоб разобрать с файлами
    position = position.strip()
    while "  " in position:
        position= position.replace("  ", " ")
    positionInList = position.split(' ')
    
    with open('file.txt', 'w') as data:
        data.write(f'{positionInList[0]}\n')
        data.write(f'{positionInList[1]}')
        data.close()
    with open("file.txt", "r") as file:
        firsPosition =  file.readline()
        secondPosition = file.readline()
    multiOfPosition = listOfNumbers[int(firsPosition)] * listOfNumbers[int(secondPosition)]
    print(multiOfPosition)

    
numberN = InputValues('Enter number N: ')
listOfNumbers = makeTheList(numberN)
print(listOfNumbers)
makeTextPositionAndMulti(listOfNumbers)


