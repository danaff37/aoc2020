import sys

a=[]
for line in sys.stdin:
    a.append(int(line))

pre=25
p=0
ns=a[p:p+pre]

p += pre
print(ns)
while len([n for n in ns if (a[p] - n) in ns and (a[p] - n) != n]) > 0:
    p += 1
    ns = a[p-pre:p]
    print(ns)
print(a[p])
