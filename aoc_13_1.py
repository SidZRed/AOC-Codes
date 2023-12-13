with open(r"input202313.txt", 'r') as file:
    data = file.read().split('\n\n')


def check(input_data):
    lines = input_data.split('\n')

    # Check symmetry line along columns
    columns = []
    for i in range(len(lines[0])):
        columns.append(''.join([lines[j][i] for j in range(len(lines))]))
    ctr = 0
    for i in range(len(columns)):
        for j in range(i+1, len(columns)):
            if columns[i] == columns[j]:
                if (i+j) % 2 == 0:
                    continue
                ctr = 1
                # Check symmetry line along columns
                a = i
                b = j
                while a <= b:
                    if columns[a] != columns[b]:
                        ctr = 0
                        break
                    a += 1
                    b -= 1
                a = i
                b = j
                while a >= 0 and b < len(columns):
                    if columns[a] != columns[b]:
                        ctr = 0
                        break
                    a -= 1
                    b += 1
            if ctr == 1:
                break
        if ctr == 1:
            break

    if ctr == 1:
        x = (i+j-1)//2
        return x+1

    # Check symmetry line along rows
    ctr = 0
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            if lines[i] == lines[j]:
                ctr = 1
                # Check symmetry line along rows
                a = i
                b = j
                while a <= b:
                    if lines[a] != lines[b]:
                        ctr = 0
                        break
                    a += 1
                    b -= 1
                a = i
                b = j
                while a >= 0 and b < len(lines):
                    if lines[a] != lines[b]:
                        ctr = 0
                        break
                    a -= 1
                    b += 1
            if ctr == 1:
                break
        if ctr == 1:
            break

    if ctr == 1:
        x = (i+j-1)//2
        return (x+1)*100

    return 0


sum = 0
for i in range(len(data)):
    sum += check(data[i])
print(sum)
