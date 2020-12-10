import sys
from itertools import combinations

a = [0]

for line in sys.stdin:
    a.append(int(line))
a.sort()
cs = []
i = 1
count = 0
ts = [0]

while i < len(a):
    if a[i] - a[i-1] == 3:
        count += 1 #for all items
        for j in range(1,len(ts) // 2 + 1): #num possible missing
            cms = combinations(ts, len(ts) - j)
            legs = [cm for cm in cms if cm[0] == ts[0] and cm[len(cm)-1] == ts[len(ts)-1]]
            for leg in legs:
                valid = True
                for k in range(1,len(leg)):
                    if leg[k] - leg[k-1] > 3:
                        valid = False
                if valid:
                    count += 1
        cs.append(count)
        count = 0
        ts.clear()
        ts.append(a[i])
    else:
        ts.append(a[i])
    i += 1

count = 1
for c in cs:
    count *= c
print(count)

