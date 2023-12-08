with open(r"C:\Users\rolla\OneDrive\Desktop\Programming\Python_proj\test03.txt", 'r') as file:
    data = file.read()
    data = data.split('\n')

import re


def has_symbol(s):
    symbols = r'[+=_ :;@#$%^&*/\\|-]'
    return re.search(symbols, s) is not None


sum_result = 0

for i in range(len(data)):
    for match in re.finditer(r'\d\d\d|\d\d|\d', data[i]):
        number_start, number_end = match.span()
        number = int(data[i][number_start:number_end])

        # Check for symbols around the number
        if number_start > 0 and has_symbol(data[i][number_start-1]):
            sum_result += number
        elif number_end < len((data[i])) and has_symbol(data[i][number_end]):
            sum_result += number
        # Check above and below the number for symbols
        elif i > 0 and has_symbol(data[i-1][number_start:number_end]):
            sum_result += number
        elif i < len(data) - 1 and has_symbol(data[i+1][number_start:number_end]):
            sum_result += number
        # Check diagonally above and below the number for symbols
        elif i > 0 and number_start > 0 and has_symbol(data[i-1][number_start-1]):
            sum_result += number
        elif i > 0 and number_end < len(data[i-1]) and has_symbol(data[i-1][number_end]):
            sum_result += number
        elif i < len(data) - 1 and number_start > 0 and has_symbol(data[i+1][number_start-1]):
            sum_result += number
        elif i < len(data) - 1 and number_end < len(data[i+1]) and has_symbol(data[i+1][number_end]):
            sum_result += number

print(sum_result)

# def has_symbol(s):
#     symbols = '+=-_:;@#$%^&*/\|'
#     for i in range(len(s)):
#         if s[i] in symbols:
#             return True
#     return False


# sum = 0
# for i in range(len(data)):
#     for j in range(len(data[i])):
#         start = end = 0
#         if data[i][j].isnumeric():
#             start = j
#             while data[i][j].isnumeric():
#                 if j == len(data[i])-1:
#                     end = j+1
#                     break
#                 j += 1
#             end = j
#             try:
#                 if data[start-1].isnumeric():
#                     continue
#             except:
#                 pass
#             # check around the number for a symbol
#             try:
#                 if data[i][start-1] in '+=-_:;@#$%^&*/\|':
#                     sum += int(data[i][start:end])
#                     continue
#             except:
#                 pass
#             try:
#                 if data[i][end] in '+=-_:;@#$%^&*/\|':
#                     sum += int(data[i][start:end])
#                     continue
#             except:
#                 pass
#             # check above and below the number for a symbol
#             try:
#                 if has_symbol(data[i-1][start:end]):
#                     sum += int(data[i][start:end])
#                     continue
#             except:
#                 pass
#             try:
#                 if has_symbol(data[i+1][start:end]):
#                     sum += int(data[i][start:end])
#                     continue
#             except:
#                 pass
#             try:
#                 if has_symbol(data[i-1][start-1]):
#                     sum += int(data[i][start:end])
#                     continue
#             except:
#                 pass
#             try:
#                 if has_symbol(data[i-1][end]):
#                     sum += int(data[i][start:end])
#                     continue
#             except:
#                 pass
#             try:
#                 if has_symbol(data[i+1][start-1]):
#                     sum += int(data[i][start:end])
#                     continue
#             except:
#                 pass
#             try:
#                 if has_symbol(data[i+1][end]):
#                     sum += int(data[i][start:end])
#                     continue
#             except:
#                 pass

# print(sum)
