# Реализуйте алгоритм перемешивания списка.

def InputValuesList (text: str):
    check = False
    listForNumbers = []
    while not check:
        try:
            number = int(input(f'{text}'))
            listForNumbers.append(number)
            if len(listForNumbers) == 5:
                check = True
        except ValueError:
            number = int(input(f'{text}'))
    return listForNumbers

def MixList(listOfNumber: list):
    
    for i in range(len(listOfNumber)):
        helpN = listOfNumber[i]
        import random
        randomN = random.randint(i,4)
        while randomN == i:
            randomN = random.randint(0,4)
        listOfNumber[i] = listOfNumber[randomN]
        listOfNumber[randomN] = helpN
    return listOfNumber

listOfNumber = InputValuesList ("Enter numbers for list: ")
print(f'Origin list: {listOfNumber}')
print(f'Mixed list: {MixList(listOfNumber)}')
