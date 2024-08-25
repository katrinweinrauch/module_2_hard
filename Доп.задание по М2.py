from typing import List

key1 = int(input('Введите число от 3 до 20: '))
key2 = []

for i in range(1, 21):
    for j in range(2, 21):
        if i == j:
            continue
        elif i > j:
            continue
        elif key1 % (i + j) == 0:
            key2.append(i)
            key2.append(j)
result = key2
print(result)
