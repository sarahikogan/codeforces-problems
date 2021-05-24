k, n, w = map(int, input().split())

c = 0

for i in range(0, w):
    c += ((i+1)*k)

print((c-n) if (c-n) >= 0 else 0)