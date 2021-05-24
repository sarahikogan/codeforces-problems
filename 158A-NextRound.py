n, k = map(int, input().split())
arr = list(map(int, input().split()))
out = 0

for i in range(n):
    if (arr[i] >= arr[k-1] and arr[i] != 0):
        out += 1

print(out)