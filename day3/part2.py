import sys

ls = []
for line in sys.stdin:
    ls.append(line)
t=[0] * 5
col=[1,3,5,7,1]
le=len(ls[0]) - 1
for i in range(1,len(ls)):
    l = ls[i]
    for j in range(0,4):
        if l[(col[j] * i) % le] == '#':
            t[j] += 1
    if (i % 2) == 0:
        if l[(col[4] * (i // 2)) % le] == '#':
            t[4] += 1

print(t)
m=1
for x in t:
    m *= x

print(m)
