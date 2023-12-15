from collections import defaultdict

with open("input202315.txt") as f:
    data = f.read()
# remove all newline charcters
data = data.replace("\n", "")
data = data.split(",")


def hash(a):
    current = 0
    for i in range(len(a)):
        current += ord(a[i])
        current *= 17
        current = current % 256
    return current


hashmap = defaultdict(list)

for i in data:
    a = 0
    while (a < len(i)):
        if i[a] == "-" or i[a] == "=":
            break
        a += 1
    if i[a] == "-":
        i = i[:a]
        h = hash(i)
        v = hashmap[h]
        for k in range(len(v)):
            if v[k][:a] == i:
                v.pop(k)
                break

    elif i[a] == "=":
        num = i[a+1:]
        i = i[:a]
        h = hash(i)
        v = hashmap[h]
        found = False
        for k in range(len(v)):
            if v[k][:a] == i:
                # Replace the num with the old num
                v[k] = i+"="+num
                found = True
                break
        if not found:
            v.append(i+"="+num)

total_power = 0
for i in hashmap.keys():
    if len(hashmap[i]) == 0:
        continue
    for j in range(len(hashmap[i])):
        power = i+1
        power *= (j+1)
        power *= int(hashmap[i][j][len(hashmap[i][j])-1])
        total_power += power

print(total_power)
