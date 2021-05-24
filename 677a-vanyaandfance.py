n, h = map(int, input().split())
arr = [int(x) for x in input().split()]

for i in arr:
    if (i > h):
        n += 1

print(n)