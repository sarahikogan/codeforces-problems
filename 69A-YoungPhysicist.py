n = int(input())
a = [0]*3
out = 0

for i in range(n):
    b = [int(y) for y in input().split()]
    for j in range(3):
        a[j] += b[j]

ans = [x for x in a if x == 0]
print("YES") if len(ans)==3 else print("NO")