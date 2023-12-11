with open(r"input202311.txt", 'r') as file:
    data = file.read().split('\n')

dup = []
for i in range(len(data)):
    if data[i] == "."*len(data[i]):
        dup.append(i)
print(dup)
for i in range(len(dup)):
    data.insert(dup[i] + i, "."*len(data[i]))


def print_data():
    for i in range(len(data)):
        print(data[i])


# Rotate data 90 degrees clockwise
data = list(zip(*data[::-1]))
# Make it back into a list of strings
data = ["".join(row) for row in data]
dup = []
for i in range(len(data)):
    if data[i] == "."*len(data[i]):
        dup.append(i)
print(dup)
for i in range(len(dup)):
    data.insert(dup[i] + i, "."*len(data[i]))

# Rotate data 90 degrees anticlockwise
data = list(zip(*data[::-1]))
data = list(zip(*data[::-1]))
data = list(zip(*data[::-1]))

data = ["".join(row) for row in data]


# print_data()


galaxy = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "#":
            galaxy.append((i, j))
# print(galaxy)
dist = 0
for i in range(len(galaxy)):
    for j in range(i+1, len(galaxy)):
        dist += abs(galaxy[i][0] - galaxy[j][0]) + \
            abs(galaxy[i][1] - galaxy[j][1])

print(dist)
