import re
    
lines = list(map(lambda x: x.replace('\n', ''), open('P1-input.txt')))

solutions = []

for i in range(0, len(lines)):
    currentLine = lines[i]
    prevLine = lines[i - 1] if i > 0 else None
    nextLine = lines[i + 1] if i < len(lines) - 1 else None

    gears = re.finditer('\*', currentLine)

    for gear in gears:
        currentLineNumbers = re.finditer('\d+', currentLine)
        prevLineNumbers = re.finditer('\d+', prevLine) if prevLine is not None else None
        nextLineNumbers = re.finditer('\d+', nextLine) if nextLine is not None else None
        gearNumbers = []

        for number in currentLineNumbers:
            if number.end() == gear.start() or number.start() == gear.end():
                gearNumbers.append(int(number.group()))
        if prevLine is not None:
            for number in prevLineNumbers:
                if number.end() - 1 in range(gear.start() - 1, gear.end() + 1) or number.start() in range(gear.start() - 1, gear.end() + 1):
                    gearNumbers.append(int(number.group()))
        if nextLine is not None:
            for number in nextLineNumbers:
                if number.end() - 1 in range(gear.start() - 1, gear.end() + 1) or number.start() in range(gear.start() - 1, gear.end() + 1):
                    gearNumbers.append(int(number.group()))


        if len(gearNumbers) == 2:
            solutions.append(gearNumbers[0] * gearNumbers[1])

print(sum(solutions))