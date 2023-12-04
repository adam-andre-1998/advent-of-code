import re

lines = list(map(lambda x: x.replace('\n', ''), open('P1-input.txt')))

i = 0
while i < len(lines):
    count = 0
    
    cardNumber = int(lines[i][5:lines[i].find(':')])
    numbers = lines[i].split(':')[1]
    winningNumbers = numbers.split('|')[0].strip().replace('  ', ' ').split(' ')
    myNumbers = numbers.split('|')[1].strip().replace('  ', ' ').split(' ')

    for number in myNumbers:
        if number in winningNumbers:
            count += 1

    for j in range(1, count + 1):
        if i + j < len(lines):
            lines.append(lines[cardNumber + j - 1])
    
    i += 1

print(len(lines))