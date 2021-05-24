s = input()

arr = []

for l in "hello":
    if (s.index(l) in arr):
        n = s.replace("l", "", 1)
        if ("l" in n):
            arr.append(n.index("l"))
        else:
            arr.append(0)
    else:
        arr.append(s.index(l))

if (sorted(arr) == arr):
    print("YES")
else:
    print("NO")