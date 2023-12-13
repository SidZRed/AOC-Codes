with open(r"input202313.txt", 'r') as file:
    data = file.read().split('\n\n')


def equate(a, b):
    return sum(x != y for x, y in zip(a, b))


def check_with_smudge(pattern):
    b = len(pattern)
    for i in range(b):
        for j in range(i + 1, b):
            ctr = equate(pattern[i], pattern[j])

            if ctr > 1:
                break

            m, n = i+1, j-1
            break_out = False

            while m <= n:
                ctr += equate(pattern[m], pattern[n])
                if ctr > 1:
                    break_out = True
                    break
                m += 1
                n -= 1

            m, n = i - 1, j + 1
            while m >= 0 and n < b:
                ctr += equate(pattern[m], pattern[n])
                if ctr > 1:
                    break_out = True
                    break
                m -= 1
                n += 1

            if break_out:
                break
            if ctr == 1:
                return (i+j+1)//2 * 100

    # Transpose the pattern
    pattern = list(map(list, zip(*pattern)))
    pattern = [''.join(pattern[i]) for i in range(len(pattern))]
    # print(pattern)

    b = len(pattern)
    for i in range(b):
        for j in range(i + 1, b):
            ctr = equate(pattern[i], pattern[j])

            if ctr > 1:
                break

            m, n = i+1, j-1
            break_out = False

            while m <= n:
                ctr += equate(pattern[m], pattern[n])
                if ctr > 1:
                    break_out = True
                    break
                m += 1
                n -= 1

            m, n = i - 1, j + 1
            while m >= 0 and n < b:
                ctr += equate(pattern[m], pattern[n])
                if ctr > 1:
                    break_out = True
                    break
                m -= 1
                n += 1

            if break_out:
                break
            if ctr == 1:
                return (i+j+1)//2

    return 0


s = len(data) + 1
for i in range(len(data)):
    s += check_with_smudge(data[i].split("\n"))
    print(check_with_smudge(data[i].split("\n")))
print(s)
