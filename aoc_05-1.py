from collections import Counter

with open(r"C:\Users\rolla\OneDrive\Desktop\Programming\Python_proj\input202105.txt", 'r') as file:
    data = file.read()
    data = data.split('\n')

c1 = []
c2 = []
for i in data:
    i = i.split("->")
    c1.append(i[0])
    c2.append(i[1])


def overlap(a, b):
    o = []
    a = a.split(",")
    b = b.split(",")
    a[0] = int(a[0])
    a[1] = int(a[1])
    b[0] = int(b[0])
    b[1] = int(b[1])
    if a[0] == b[0]:
        for i in range(min(a[1], b[1]), max(a[1], b[1])+1):
            o.append((a[0], i))
    elif a[1] == b[1]:
        for i in range(min(a[0], b[0]), max(a[0], b[0])+1):
            o.append((i, a[1]))
    elif a[0]-b[0] == a[1]-b[1]:
        slope = (a[0]-b[0])/(a[1]-b[1])
        if slope == 1:
            for i in range(max(a[0], b[0]) - min(a[0], b[0])+1):
                o.append((min(a[0], b[0])+i, min(a[1], b[1])+i))
        elif slope == -1:
            for i in range(max(a[0], b[0]) - min(a[0], b[0])+1):
                o.append((min(a[0], b[0])+i, max(a[1], b[1])-i))
    return o


# print(overlap("976,35", "976,987"))
coords = []
for i in range(len(c1)):
    coords.extend(overlap(c1[i], c2[i]))
# print(coords)
element_counts = Counter(coords)

duplicates = [element for element,
              count in element_counts.items() if count > 1]

print(len(duplicates))
