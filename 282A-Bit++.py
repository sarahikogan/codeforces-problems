x = 0

for _ in range(int(input())):
    st = input()

    if ("--" in st):
        x -= 1

    if ("++" in st):
        x += 1

print(x)