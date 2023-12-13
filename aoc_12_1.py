
with open(r"input202312.txt", 'r') as file:
    data = file.read().split('\n')

for i in range(len(data)):
    data[i] = data[i].split(" ")


def valid(x, order):
    counts = []
    current_count = 0

    for char in x:
        if char == '#':
            current_count += 1
        elif char == '.':
            if current_count > 0:
                counts.append(current_count)
                current_count = 0

    # Check if the last sequence ends with '#'
    if current_count > 0:
        counts.append(current_count)

    return counts == order


def generate_permutations(x, y):
    permutations = []
    if x == 1 and y == 0:
        return "."
    elif x == 0 and y == 1:
        return "#"
    if x > 0:
        for p in generate_permutations(x-1, y):
            permutations.append("." + p)
    if y > 0:
        for p in generate_permutations(x, y-1):
            permutations.append("#" + p)
    return permutations


def permutations(a):
    springs = a[0]
    springs = list(springs)
    order = a[1].split(",")
    for i in range(len(order)):
        order[i] = int(order[i])
    total = 0
    for i in order:
        total += i
    # "#" = broken
    # "." = working
    # "?" = unknown

    # Remove all the working springs from the beginning and the end
    while springs[0] == ".":
        springs.pop(0)
    while springs[-1] == ".":
        springs.pop(-1)

    y = total - springs.count("#")
    x = springs.count("?") - y

    p = generate_permutations(x, y)
    count = 0
    # Construct possible permutations by replacing "?" with the permutations generated
    for i in p:
        springs_copy = springs.copy()
        m = n = 0
        while m < len(springs_copy):
            if springs_copy[m] == "?":
                springs_copy[m] = i[n]
                n += 1
            m += 1
        if valid(springs_copy, order):
            count += 1
    return count


ctr = 0
for i in data:
    ctr += permutations(i)

print(ctr)
