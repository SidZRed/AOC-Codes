from collections import Counter

with open(r"C:\Users\rolla\Downloads\input_test.txt", 'r') as file:
    data = file.read()
    data = data.split('\n')

hands = []
for i in range(len(data)):
    hands.append(data[i][0:data[i].index(' ')])

bets = {}
for i in range(len(data)):
    bets[hands[i]] = data[i][data[i].index(' ') + 1:]


def value_1(hand1):
    hand = list(hand1)
    char_count = Counter(hand)

    most_common_char, freq = char_count.most_common(1)[0]

    if most_common_char == 'J' and len(char_count) > 1:
        most_common_char, freq = char_count.most_common(2)[1]

    hand = [most_common_char if char == 'J' else char for char in hand]
    hand.sort()

    # Five of a kind
    if hand.count(hand[0]) == 5:
        return 7
    # Four of a kind
    if hand.count(hand[2]) == 4:
        return 6
    # Full house
    if (hand[0] == hand[1] and hand[2] == hand[3] == hand[4]) or (hand[0] == hand[1] == hand[2] and hand[3] == hand[4]):
        return 5
    # Three of a kind
    if hand.count(hand[2]) == 3:
        return 4
    # Two pairs
    if (hand[0] == hand[1] and hand[2] == hand[3]) or (hand[0] == hand[1] and hand[3] == hand[4]) or (hand[1] == hand[2] and hand[3] == hand[4]):
        return 3
    # One pair
    if hand[0] == hand[1] or hand[1] == hand[2] or hand[2] == hand[3] or hand[3] == hand[4]:
        return 2
    # High card
    return 1


def comp(hand):
    val = {
        'A': 2,
        'K': 3,
        'Q': 4,
        "J": 15,
        'T': 6,
        '9': 7,
        '8': 8,
        '7': 9,
        '6': 10,
        '5': 11,
        '4': 12,
        '3': 13,
        '2': 14,
    }
    t = 0
    x = 0
    for i in hand:
        t += 100**(5-x)*val[i]
        x += 1

    return -t


hands = sorted(hands, key=lambda x: (value_1(x), comp(x)))
total = 0
for i in range(len(hands)):
    total += (i+1)*int(bets[hands[i]])

# for i in hands:
#     print(i, value_1(i), comp(i))
print(total)
