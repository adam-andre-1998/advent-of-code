f = open("P1-input.txt")

possibleValues = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SHIFT_CONVERSION = 9
numbers = []

for line in f:
    indexWhereFoundArray = list(map(lambda x: line.find(x), possibleValues))
    lastIndexWhereFoundArray = list(map(lambda x: line.rfind(x), possibleValues))

    number1 = possibleValues[indexWhereFoundArray.index(min(i for i in indexWhereFoundArray if i >= 0))]
    number2 = possibleValues[lastIndexWhereFoundArray.index(max(lastIndexWhereFoundArray))]

    if (len(number1) > 1):
        number1 = possibleValues[possibleValues.index(number1) + SHIFT_CONVERSION]

    if (len(number2) > 1):
        number2 = possibleValues[possibleValues.index(number2) + SHIFT_CONVERSION]

    numbers.append(int(f'{number1}{number2}'))

print(sum(numbers))