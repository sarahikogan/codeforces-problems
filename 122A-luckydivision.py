n = int(input())
out = "NO"

arr = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

for i in arr:
    if (n%i == 0):
        out = "YES"

print(out)