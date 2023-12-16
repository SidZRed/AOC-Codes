with open("input202316.txt") as f:
    data = f.read().split("\n")

directions = ["up", "right", "down", "left"]
grid = {}
for i in range(len(data)):
    for j in range(len(data[i])):
        for k in directions:
            grid[(i, j, k)] = 0


def reflect(direction, mirror):
    if mirror == "/":
        if direction == "up":
            return "right"
        elif direction == "right":
            return "up"
        elif direction == "down":
            return "left"
        elif direction == "left":
            return "down"
    elif mirror == "\\":
        if direction == "up":
            return "left"
        elif direction == "left":
            return "up"
        elif direction == "down":
            return "right"
        elif direction == "right":
            return "down"


def trace(start_x, start_y, start_direct):
    global grid
    visited = [(start_x, start_y, start_direct)]
    while visited:
        x, y, direct = visited.pop()
        if x < 0 or y < 0 or x >= len(data) or y >= len(data[0]) or grid[(x, y, direct)] > 0:
            continue
        if data[x][y] == ".":
            grid[(x, y, direct)] += 1
        elif data[x][y] == "/":
            grid[(x, y, direct)] += 1
            direct = reflect(direct, "/")
        elif data[x][y] == "\\":
            grid[(x, y, direct)] += 1
            direct = reflect(direct, "\\")
        elif data[x][y] == "-":
            if direct == "right" or direct == "left":
                grid[(x, y, direct)] += 1
            else:
                grid[(x, y, direct)] += 1
                visited.append((x, y+1, "right"))
                visited.append((x, y-1, "left"))
                continue
        elif data[x][y] == "|":
            if direct == "up" or direct == "down":
                grid[(x, y, direct)] += 1
            else:
                grid[(x, y, direct)] += 1
                visited.append((x+1, y, "down"))
                visited.append((x-1, y, "up"))
                continue
        if direct == "right":
            visited.append((x, y+1, direct))
        elif direct == "left":
            visited.append((x, y-1, direct))
        elif direct == "up":
            visited.append((x-1, y, direct))
        elif direct == "down":
            visited.append((x+1, y, direct))


def energize(a, b, direct):
    directions = ["up", "right", "down", "left"]
    for i in range(len(data)):
        for j in range(len(data[i])):
            for k in directions:
                grid[(i, j, k)] = 0
    trace(a, b, direct)
    ctr = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if grid[(i, j, "right")] > 0 or grid[(i, j, "left")] > 0 or grid[(i, j, "up")] > 0 or grid[(i, j, "down")] > 0:
                ctr += 1
    return ctr


energies = []

for i in range(len(data)):
    energies.append(energize(i, 0, "right"))
    energies.append(energize(i, len(data[0])-1, "left"))

for i in range(len(data[0])):
    energies.append(energize(0, i, "down"))
    energies.append(energize(len(data)-1, i, "up"))

print("Part 2:", max(energies))
