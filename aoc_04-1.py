from collections import defaultdict

with open(r"C:\Users\rolla\OneDrive\Desktop\Programming\Python_proj\input202304.txt", 'r') as file:
    data = file.read()
    data = data.split('\n')

bar = data[0].index("|")
colon = data[0].index(":")


def score(card):
    lucky = card[colon:bar]
    you = card[bar+1:]
    lucky = lucky.split(" ")
    you = you.split(" ")
    i = 0
    while (i < len(lucky)):
        if lucky[i] == '':
            lucky.pop(i)
        else:
            i += 1
    i = 0
    while (i < len(you)):
        if you[i] == '':
            you.pop(i)
        else:
            i += 1

    s = 0
    for i in you:
        if i in lucky:
            s += 1
    return s


cards = defaultdict(int)
for i in range(len(data)):
    cards[i] = 1

for i in range(len(data)):
    a = score(data[i])
    for j in range(i+1, i+1+a):
        cards[j] += cards[i]

s = 0
for i in range(len(data)):
    s += cards[i]
print(s)
