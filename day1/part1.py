import sys

a=[]
for line in sys.stdin:
    a.append(int(line))

for val in a:
    for val2 in a:
        if val == val2:
            continue
        if val + val2 == 2020:
            print(val,val2,val*val2)
