import re
    
lines = list(map(lambda x: x.replace('\n', ''), open('P1-input.txt')))

symbols = ['$', '*', '/', '@', '+', '-', '%', '#', '&', '=']
solutions = []

for i in range(0, len(lines)):
    currentLine = lines[i]
    prevLine = lines[i - 1] if i > 0 else None
    nextLine = lines[i + 1] if i < len(lines) - 1 else None

    numbers = re.finditer('\d+', lines[i])

    for number in numbers:
        rangeStart = number.start() if number.start() == 0 else number.start() - 1
        rangeEnd = number.end() if number.end() == len(currentLine) else number.end() + 1

        for j in range(rangeStart, rangeEnd):
            if currentLine[j] in symbols:
                solutions.append(int(number.group()))
                break
            if prevLine is not None and prevLine[j] in symbols:
                solutions.append(int(number.group()))
                break
            if nextLine is not None and nextLine[j] in symbols:
                solutions.append(int(number.group()))
                break

print(sum(solutions))