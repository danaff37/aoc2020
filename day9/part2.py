import sys

a=[]
for line in sys.stdin:
    a.append(int(line))

pre=25
p=0
ns=a[p:p+pre]

p += pre
while len([n for n in ns if (a[p] - n) in ns and (a[p] - n) != n]) > 0:
    p += 1
    ns = a[p-pre:p]

mi = -1
ma = 0
for i in range(0,len(a)):
    mi = -1
    ma = 0
    sum = 0
    while sum < a[p]:
        for j in range(i,len(a)):
            sum += a[j]
            if a[j] > ma: ma = a[j]
            if a[j] < mi or mi < 0: mi = a[j]
            if sum >= a[p]:
                break
        if sum == a[p]:
            break
    if sum == a[p]:
        break

print(mi,ma, mi + ma)
