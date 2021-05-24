n = int(input())
arr = []
ansarr = []
out = 0

for i in range(n):
    arr.append([int(i) for i in input().split()])

for i in range(n):
    out -= arr[i][0]
    out += arr[i][1]
    ansarr.append(out)

print(max(ansarr))
