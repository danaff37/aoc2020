import sys
import re

a=0
b=['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
b.sort()
c=[]
for line in sys.stdin:
    if line.strip():
        for d in b:
            if re.search(r'\b' + d + ':', line):
                c.append(d)
    else:
        c.sort()
        if b == c:
            a += 1
        c.clear()
c.sort()
if b == c:
    a += 1
print(a)
