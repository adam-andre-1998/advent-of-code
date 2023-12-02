f = open('P1-input.txt')
possibleRed = 12
possibleGreen = 13
possibleBlue = 14

gameIdList = []

for line in f:
    parts = line.split(':')
    gameId = int(parts[0][5:])

    draws = parts[1].split(';')

    failed = False

    for draw in draws:
        red = 0
        green = 0
        blue = 0

        colors = draw.split(',')
        for color in colors:
            color = color.strip()
            if 'blue' in color:
                blue = int(color[0:color.find('b')])
            elif 'green' in color:
                green = int(color[0:color.find('g')])
            elif 'red' in color:
                red = int(color[0:color.find('r')])

        if red > possibleRed or green > possibleGreen or blue > possibleBlue:
            failed = True
    
    if not failed:
        gameIdList.append(gameId)

print(sum(gameIdList))