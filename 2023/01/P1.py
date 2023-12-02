f = open("P1-input.txt")

numbers = []

numbersDict = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

for line in f:
    possibleValues = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    indexWhereFoundArray = list(map(lambda x: line.find(x), possibleValues))
    lastIndexWhereFoundArray = list(map(lambda x: line.rfind(x), possibleValues))

    number1 = possibleValues[indexWhereFoundArray.index(min(i for i in indexWhereFoundArray if i >= 0))]
    number2 = possibleValues[lastIndexWhereFoundArray.index(max(lastIndexWhereFoundArray))]

    if (number1 in numbersDict):
        number1 = numbersDict[number1]

    if (number2 in numbersDict):
        number2 = numbersDict[number2]

    numbers.append(int(f'{number1}{number2}'))

print(sum(numbers))