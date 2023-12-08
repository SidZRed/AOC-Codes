with open(r"C:\Users\rolla\OneDrive\Desktop\Programming\Python_proj\input202303.txt", 'r') as file:
    data = file.read()
    data = data.split('\n')


def get_num(a, b):
    if data[a][b].isnumeric():
        start = b
        end = b

        # Find the start index of the numeric value
        while start > 0 and data[a][start-1].isnumeric():
            start -= 1

        # Find the end index of the numeric value
        while end < len(data[0])-1 and data[a][end+1].isnumeric():
            end += 1

        # Extract the numeric value
        return int(data[a][start:end+1])
    else:
        return 0


def gear_ratio(a, b):
    numbers = []

    # Left
    if b >= 1 and data[a][b-1].isnumeric():
        numbers.append(get_num(a, b-1))

    # Right
    if b < len(data[a])-1 and data[a][b+1].isnumeric():
        numbers.append(get_num(a, b+1))

    # Up
    if a >= 1 and data[a-1][b].isnumeric():
        numbers.append(get_num(a-1, b))

    # Down
    if a < len(data)-1 and data[a+1][b].isnumeric():
        numbers.append(get_num(a+1, b))

    # Up left
    if a >= 1 and b >= 1 and data[a-1][b-1].isnumeric():
        numbers.append(get_num(a-1, b-1))

    # Up right
    if a >= 1 and b < len(data[a])-1 and data[a-1][b+1].isnumeric():
        numbers.append(get_num(a-1, b+1))

    # Down left
    if a < len(data)-1 and b >= 1 and data[a+1][b-1].isnumeric():
        numbers.append(get_num(a+1, b-1))

    # Down right
    if a < len(data)-1 and b < len(data[a])-1 and data[a+1][b+1].isnumeric():
        numbers.append(get_num(a+1, b+1))

    numbers.sort()
    # extract first and second non-zero numbers
    first = second = 0
    for i in range(len(numbers)):
        if numbers[i] != 0:
            first = numbers[i]
            break
    for i in range(len(numbers)):
        if numbers[i] != 0 and numbers[i] != first:
            second = numbers[i]
            break
    return first*second


sum = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '*':
            sum += gear_ratio(i, j)

print(sum)
