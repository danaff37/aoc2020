import sys
import re

bags={}
for line in sys.stdin:
    ms = re.findall(r'([0-9]*)? ?(\w* \w*) bag', line)
    key = ms[0][1]
    bags[key] = []
    for i in range(1,len(ms)):
        bags[key].append(ms[i][1])
fs = ['shiny gold']
c = [];
while len(fs) > 0:
    newfs = []
    for f in fs:
        bs = [i[0] for i in bags.items() if f in i[1]]
        for b in bs:
            if b not in fs and b not in newfs:
                if b not in c: c.append(b)
                print(b)
                newfs.append(b)

    fs.clear()
    fs = newfs
print(len(c))
