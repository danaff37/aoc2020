import sys
import re

bags={}
for line in sys.stdin:
    ms = re.findall(r'([0-9]*)? ?(\w* \w*) bag', line)
    key = ms[0][1]
    bags[key] = []
    for i in range(1,len(ms)):
        if ms[i][0]:
            for j in range(0,int(ms[i][0])):
                bags[key].append(ms[i][1])
fs = ['shiny gold']
d = 0
while len(fs) > 0:
    newfs = []
    for f in fs:
        bs = bags[f]
        d += len(bs)
        for b in bs:
            newfs.append(b)

    fs.clear()
    fs = newfs
print(d)
