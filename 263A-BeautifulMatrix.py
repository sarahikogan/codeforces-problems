# 1. take inputs

matrix = []

for x in range(5):
    matrix.append([int(y) for y in input().split()])
# 2. get the 1 to row 3

for i in matrix:
    if 1 in i:
        v = matrix.index(i)
        h = i.index(1)

steps = abs(2 - v) + abs(2 - h)

print(steps)
