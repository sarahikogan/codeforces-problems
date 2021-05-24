n = int(input())
arr = []
for x in range(n): arr.append(int(input()))

out = 1
a = arr[0]
for i in arr:
    if (i != a):
        out += 1
        a = i

print(out)