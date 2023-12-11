with open(r"input202311.txt", 'r') as file:
    data = file.read().split('\n')
dup1 = []
for i in range(len(data)):
    if data[i] == "."*len(data[i]):
        dup1.append(i)


# Rotate data 90 degrees clockwise
data = list(zip(*data[::-1]))
# Make it back into a list of strings
data = ["".join(row) for row in data]


dup2 = []
for i in range(len(data)):
    if data[i] == "."*len(data[i]):
        dup2.append(i)

# Rotate data 90 degrees anticlockwise
data = list(zip(*data[::-1]))
data = list(zip(*data[::-1]))
data = list(zip(*data[::-1]))
data = ["".join(row) for row in data]


print(dup1)
print(dup2)


galaxy = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "#":
            galaxy.append((i, j))

# Calculate the distance between each pair of stars
dist = 0
for i in range(len(galaxy)):
    for j in range(i+1, len(galaxy)):
        # Calculate the number of elements in dup between the two stars
        hidden = 0
        for k in range(min(galaxy[i][0], galaxy[j][0]), max(galaxy[i][0], galaxy[j][0])):
            if k in dup1:
                hidden += 1
        for k in range(min(galaxy[i][1], galaxy[j][1]), max(galaxy[i][1], galaxy[j][1])):
            if k in dup2:
                hidden += 1
        dist += abs(galaxy[i][0] - galaxy[j][0]) + \
            abs(galaxy[i][1] - galaxy[j][1])
        dist += hidden*999999
        # print(hidden)

print(dist)
