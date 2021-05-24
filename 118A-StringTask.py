s = input().lower()
vowels = ['a','e','i','o','u','y']

n = ""

for l in s:
    if (l not in vowels):
        n += "." + l

print(n)