import re

lines = list(map(lambda x: x.replace('\n', ''), open('P1-input.txt')))

solutions = []

for line in lines:
    count = 0
    numbers = line.split(':')[1]
    winningNumbers = numbers.split('|')[0].strip().replace('  ', ' ').split(' ')
    myNumbers = numbers.split('|')[1].strip().replace('  ', ' ').split(' ')
    for number in myNumbers:
        if number in winningNumbers:
            count = 1 if count == 0 else count * 2
    solutions.append(count)

print(sum(solutions))