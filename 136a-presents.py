n = int(input())
arr = [int(x) for x in input().split()]

out = [0]*n

for i in arr:
    print(out[i-1], arr[i-1])
    out[i-1] = arr[i-1]

'''

'''
print(out)