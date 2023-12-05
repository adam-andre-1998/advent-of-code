import re

lines = list(map(lambda x: x.replace('\n', ''), open('P1-input.txt')))
seeds = list(map(lambda x: int(x), lines[0].split(':')[1].strip().split(' ')))

mapIndexes = []
for i in range(len(lines)):
    if re.match('[a-z]', lines[i]):
        mapIndexes.append(i)
mapIndexes = mapIndexes[1:len(mapIndexes)]

def getFirstSeedRange(seeds):
    evenSeeds = seeds[::2]
    oddSeeds = seeds[1::2]
    seedRanges = []
    for i in range(len(evenSeeds)):
        seedRanges.append(range(evenSeeds[i], evenSeeds[i] + oddSeeds[i], 1000000))
    allSeeds = []
    for seedRange in seedRanges:
        allSeeds += [*seedRange]
    return allSeeds
    
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

def getMappedValueReversed(location, destinationStart, sourceStart, rangeLength):
    destinationRange = range(destinationStart, destinationStart + rangeLength)

    difference = destinationStart - sourceStart

    if location in destinationRange:
        return location - difference
    return None

def mapLocationToSeed(location):
    for i in range(len(mapIndexes) - 1, -1, -1):
        mappedNumber = location

        if i == len(mapIndexes) - 1:
            for j in range(mapIndexes[i] + 1, len(lines)):
                parts = re.findall('\d+', lines[j])
                mvr = getMappedValueReversed(mappedNumber, int(parts[0]), int(parts[1]), int(parts[2]))
                if mvr is not None:
                    mappedNumber = mvr
                    break
            
        else:
            for j in range(mapIndexes[i] + 1, mapIndexes[i + 1] - 1):
                parts = re.findall('\d+', lines[j])
                mvr = getMappedValueReversed(mappedNumber, int(parts[0]), int(parts[1]), int(parts[2]))
                if mvr is not None:
                    mappedNumber = mvr
                    break

        location = mappedNumber

    return location

def solutionForSeedList(seedList):
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


approx1 = solutionForSeedList(getFirstSeedRange(seeds))
approx1 = mapLocationToSeed(approx1)

approx2 = solutionForSeedList([*range(approx1 - 1000000, approx1 + 1000000, 100000)])
approx2 = mapLocationToSeed(approx2)

approx3 = solutionForSeedList([*range(approx2 - 100000, approx2 + 100000, 10000)])
approx3 = mapLocationToSeed(approx3)

approx4 = solutionForSeedList([*range(approx3 - 10000, approx3 + 10000, 1000)])
approx4 = mapLocationToSeed(approx4)

approx5 = solutionForSeedList([*range(approx4 - 1000, approx4 + 1000, 100)])
approx5 = mapLocationToSeed(approx5)

approx6 = solutionForSeedList([*range(approx5 - 100, approx5 + 100, 10)])
approx6 = mapLocationToSeed(approx6)

approx7 = solutionForSeedList([*range(approx6 - 10, approx6 + 100, 1)])
print(approx7)