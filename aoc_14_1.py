with open(r"file_name.txt", 'r') as file:
    data = file.read().split('\n')
data = [list(i) for i in data]


def move_up(data):
    for a in range(len(data)):
        for b in range(len(data[0])):
            if data[a][b] == "O":
                i = a-1
                while i >= 0:
                    if data[i][b] == ".":
                        data[i][b] = "O"
                        data[i+1][b] = "."
                    if data[i][b] == "#":
                        break
                    i -= 1


def rotate(grid):
    n = len(grid)
    m = len(grid[0])
    new_grid = [["." for j in range(n)] for i in range(m)]
    for i in range(n):
        for j in range(m):
            new_grid[j][n - i - 1] = grid[i][j]
    return new_grid


def cycle(data):
    for a in range(4):
        move_up(data)
        data = rotate(data)


def get_score(grid):
    n = len(grid)
    ans = 0
    for i in range(n):
        ans += (n - i) * grid[i].count("O")
    return ans


# Find cycle:
for i in range(1000):
    cycle(data)
a = get_score(data)
for i in range(200):
    cycle(data)
    if get_score(data) == a:
        print(i)
        break
print(get_score(data))

# Calculate by using length of cycle
