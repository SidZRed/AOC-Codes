import math


def find_lcm(numbers):
    return math.lcm(*numbers)


with open(r"C:\Users\rolla\OneDrive\Desktop\Programming\Python_proj\input202308.txt", 'r') as file:
    data = file.read().split('\n')

code = data[0]
places = {}

for i in data[2:]:
    places[i[0:3]] = (i[7:10], i[12:15])


def move(place, direction):
    if direction == "L":
        return places[place][0]
    elif direction == "R":
        return places[place][1]


start = []
for i in data[2:]:
    if i[2] == "A":
        start.append(i[0:3])


def valid(a):
    return a[2] == "Z"


paths = []
for j in start:
    i = 0
    ctr = 0
    while (i < len(code)):
        j = move(j, code[i])
        i += 1
        ctr += 1
        if valid(j):
            paths.append(ctr)
            break
        if i == len(code):
            i = 0

print(paths)
print(find_lcm(paths))
