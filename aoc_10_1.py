with open(r"input202310.txt", 'r') as file:
    data = file.read().split('\n')

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "S":
            start = (i, j+1)
            break
direction = "right"


def move(a, b):
    global direction
    # print(a, b)
    if direction == "right":
        if data[a][b] == "-":
            return (a, b + 1)
        if data[a][b] == "J":
            direction = "up"
            return (a - 1, b)
        if data[a][b] == "7":
            direction = "down"
            return (a + 1, b)
    if direction == "left":
        if data[a][b] == "-":
            return (a, b - 1)
        if data[a][b] == "L":
            direction = "up"
            return (a - 1, b)
        if data[a][b] == "F":
            direction = "down"
            return (a + 1, b)
    if direction == "up":
        if data[a][b] == "|":
            return (a - 1, b)
        if data[a][b] == "F":
            direction = "right"
            return (a, b + 1)
        if data[a][b] == "7":
            direction = "left"
            return (a, b - 1)
    if direction == "down":
        if data[a][b] == "|":
            return (a + 1, b)
        if data[a][b] == "L":
            direction = "right"
            return (a, b + 1)
        if data[a][b] == "J":
            direction = "left"
            return (a, b - 1)


loop = []

while True:

    loop.append(start)
    start = move(start[0], start[1])
    if data[start[0]][start[1]] == "S":
        break
# print(loop)
loop.append(start)
loop = sorted(loop, key=lambda x: (x[0], x[1]))

data = [['.' if (row, column) not in loop else data[row][column]
         for column in range(len(data[row]))] for row in range(len(data))]


interior = 0
for row in data:
    for i, char in enumerate(row):
        if char != ".":
            continue

        intersect = 0
        corner_pipes = []
        for j in range(i + 1, len(row)):
            if row[j] in "|":
                intersect += 1
            if row[j] in "FL":
                corner_pipes.append(row[j])
            if len(corner_pipes) != 0 and row[j] == "J" and corner_pipes[-1] == "F" or row[j] == "7" and corner_pipes[-1] == "L":
                corner_pipes.pop(-1)
                intersect += 1

        if intersect % 2 == 1:
            interior += 1

print(interior)
