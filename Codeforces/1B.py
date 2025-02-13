import re


def convert_to_alphabetic(num):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while num > 0:
        num -= 1
        result = alphabet[num % 26] + result
        num //= 26
    return result


def convert_to_numeric(s):
    total = 0
    for char in s:
        if char.isalpha():
            total = total * 26 + ord(char) - ord('A') + 1
    return total


inputs = []
n = int(input())
for _ in range(n):
    inputs.append(input())

results = []
for entry in inputs:
    if re.match(r'R\d+C\d+', entry):
        r, c = map(int, re.findall(r'R(\d+)C(\d+)', entry)[0])
        results.append(convert_to_alphabetic(c) + f'{r}')
    else:
        alpha_part = re.findall(r'[A-Z]+', entry)[0]
        num_part = re.findall(r'\d+', entry)[0]
        results.append(f'R{num_part}C{convert_to_numeric(alpha_part)}')

for result in results:
    print(result)