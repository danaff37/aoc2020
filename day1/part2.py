import sys

a=[]
for line in sys.stdin:
    a.append(int(line))

for v1 in a:
    for v2 in a:
        for v3 in a:
            if v1 + v2 + v3 == 2020:
                print(v1,v2,v3,v1*v2*v3)
