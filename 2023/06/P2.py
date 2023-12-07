import re

lines = list(map(lambda x: x.replace('\n', ''), open('P1-input.txt')))

time = lines[0].split(':')[1].strip()
time = int(re.sub(' +', '', time))

distance = lines[1].split(':')[1].strip()
distance = int(re.sub(' +', '', distance))

count = 0
for j in range(0, time + 1):
    speed = j
    remainingSeconds = time - j
    calculatedDistance = speed * remainingSeconds
    if calculatedDistance > distance:
        count += 1

print(count)