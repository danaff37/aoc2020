import sys

ls = []
for line in sys.stdin:
    ls.append(line)
t=0
col=3
for l in ls[1:]:
    if l[col] == '#':
        t += 1
    col += 3
    col = col % (len(l) - 1)

print(t)
