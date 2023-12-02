f = open('day2-2023-input.txt')

powerList = []

for line in f:
    parts = line.split(':')
    draws = parts[1].split(';')
    maxRed = 0
    maxBlue = 0
    maxGreen = 0

    for draw in draws:
        colors = draw.split(',')
        for color in colors:
            color = color.strip()
            if 'blue' in color:
                blue = int(color[0:color.find('b')])
                if blue > maxBlue:
                    maxBlue = blue
            elif 'green' in color:
                green = int(color[0:color.find('g')])
                if green > maxGreen:
                    maxGreen = green
            elif 'red' in color:
                red = int(color[0:color.find('r')])
                if red > maxRed:
                    maxRed = red

    powerList.append(maxRed * maxGreen * maxBlue)

print(sum(powerList))