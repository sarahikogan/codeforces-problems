n = int(input())
arr = []
c = 0
for i in range(n):
    arr += [input().split()]

for i in arr:
    if (int(i[0]) <= int(i[1])-2):
        c += 1


print(c)