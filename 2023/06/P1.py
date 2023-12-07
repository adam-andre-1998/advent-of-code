import re

lines = list(map(lambda x: x.replace('\n', ''), open('P1-input.txt')))

times = lines[0].split(':')[1].strip()
times = re.sub(' +', ' ', times)
times = list(map(lambda x: int(x), times.split(' ')))

distances = lines[1].split(':')[1].strip()
distances = re.sub(' +', ' ', distances)
distances = list(map(lambda x: int(x), distances.split(' ')))

waysToBeat = []

for i in range(0, len(times)):
    count = 0

    for j in range(0, times[i] + 1):
        speed = j
        remainingSeconds = times[i] - j
        distance = speed * remainingSeconds
        if distance > distances[i]:
            count += 1

    waysToBeat.append(count)

result = 1
for x in waysToBeat:
    result = result * x

print(result)