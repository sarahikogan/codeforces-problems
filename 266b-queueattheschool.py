n, t = map(int, input().split())
s = input()

while t > 0:
    s = s.replace('BG','GB')
    t -= 1

print(s)