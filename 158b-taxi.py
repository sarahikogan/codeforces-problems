n = int(input())
arr = sorted([int(x) for x in input().split()])
narr = [0] * n

print(arr)

t = 0
out = 0
for i in range(len(arr)):
    t = arr[i]
    if ((4 - t) in arr[i:]):
        print(4-t)

    
print(out)