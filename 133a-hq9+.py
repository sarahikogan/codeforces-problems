s = list(input())
out = "NO"

for l in s:
    if (l=='H' or l=='Q' or l=='9'):
        out = "YES"

print(out)