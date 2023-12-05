import re

lines = list(map(lambda x: x.replace('\n', ''), open('P1-input.txt')))
seeds = list(map(lambda x: int(x), lines[0].split(':')[1].strip().split(' ')))

mapIndexes = []
for i in range(len(lines)):
    if re.match('[a-z]', lines[i]):
        mapIndexes.append(i)

mapIndexes = mapIndexes[1:len(mapIndexes)]

def getMappedValues(seeds, destinationStart, sourceStart, rangeLength):
    mappedSeeds = []
    notMappedSeeds = []

    sourceRange = range(sourceStart, sourceStart + rangeLength)
    destinationRange = range(destinationStart, destinationStart + rangeLength)

    for seed in seeds:
        if seed in sourceRange:
            mappedSeeds.append(destinationRange[seed - sourceStart])
        else:
            notMappedSeeds.append(seed)

    return [mappedSeeds, notMappedSeeds]

def solutionForList(seedList):
    for i in range(len(mapIndexes)):
        notMapped = seedList
        mapped = []
        if i == len(mapIndexes) - 1:
            for j in range(mapIndexes[i] + 1, len(lines)):
                parts = re.findall('\d+', lines[j])
                mappedValues = getMappedValues(notMapped, int(parts[0]), int(parts[1]), int(parts[2]))
                notMapped = list(set(notMapped) & set(mappedValues[1]))
                mapped += mappedValues[0]
            
        else:
            for j in range(mapIndexes[i] + 1, mapIndexes[i + 1] - 1):
                parts = re.findall('\d+', lines[j])
                mappedValues = getMappedValues(notMapped, int(parts[0]), int(parts[1]), int(parts[2]))
                notMapped = list(set(notMapped) & set(mappedValues[1]))
                mapped += mappedValues[0]
        
        seedList = mapped + notMapped
    return min(seedList)

print(solutionForList(seeds))