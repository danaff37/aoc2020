import sys

a=[0]
for line in sys.stdin:
    a.append(int(line))
a.sort()

threes = 1
ones = 0
for i in range(1,len(a)):
    if a[i] - a[i-1] == 1: ones += 1
    elif a[i] - a[i-1] == 3: threes += 1
print(threes*ones)
