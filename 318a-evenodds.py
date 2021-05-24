n, k = map(int, input().split())


seq = []
for i in range(n):
    if (i%2==1):
        seq.append(i)
for i in range(n):
    if (i%2==0):
        seq.append(i)    

print(seq[k-1])