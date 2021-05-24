n = int(input())
s = input()
c = 0

for x in range(0, n-1):
    if (s[x] == s[x+1]):
       c += 1

print(c)
