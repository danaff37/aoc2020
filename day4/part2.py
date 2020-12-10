import sys
import re

a=0
b=['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
b.sort()
c=[]
for line in sys.stdin:
    print('!!'+line.strip()+'!!')
    if line.strip():
        for d in b:
            mat = re.match(r'.*\b' + d + ':([^\s]*).*', line)
            if not mat:
                #print('no match')
                continue
            print(mat.groups()[0])
            if d == 'byr':
                try:
                    byr=int(mat.groups()[0])
                    if 1920 <= byr <= 2002:
                        print('valid byr', byr)
                        c.append(d)
                    else:
                        print('invalid byr', byr)
                except:
                    print('bad byr')
                    continue
            elif d == 'iyr':
                try:
                    iyr=int(mat.groups()[0])
                    if 2010 <= iyr <= 2020:
                        print('valid iyr', iyr)
                        c.append(d)
                    else:
                        print('invalid iyr', iyr)
                except:
                    print('bad iyr')
                    continue
            elif d == 'eyr':
                try:
                    eyr=int(mat.groups()[0])
                    if 2020 <= eyr <= 2030:
                        print('valid eyr', eyr)
                        c.append(d)
                    else:
                        print('invalid eyr', eyr)
                except:
                    print('bad eyr')
                    continue
            elif d == 'hgt':
                hgts = re.match(r'([0-9]+)(in|cm)',mat.groups()[0])
                try:
                    hgt = int(hgts.groups()[0])
                    if hgts.groups()[1] == 'in' and (59 <= hgt <= 76):
                        print('valid hgt in',hgt)
                        c.append(d)
                    elif hgts.groups()[1] == 'cm' and (150 <= hgt <= 193):
                        print('valid hgt cm',hgt)
                        c.append(d)
                    else:
                        print('invalid hgt', mat.groups()[0])
                except:
                    print('hgt exception')
                    continue
            elif d == 'hcl':
                if re.match(r'#[0-9a-f]{6}', mat.groups()[0]):
                    print('valid hcl',mat.groups()[0])
                    c.append(d)
                else:
                    print('invalid hcl',mat.groups()[0])
            elif d == 'ecl':
                if mat.groups()[0] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    print('valid ecl',mat.groups()[0])
                    c.append(d)
                else:
                    print('invalid ecl',mat.groups()[0])
            elif d == 'pid':
                if re.match(r'^[0-9]{9}$', mat.groups()[0]):
                    print('valid pid',mat.groups()[0])
                    c.append(d)
                else:
                    print('invalid pid',mat.groups()[0])

    else:
        print('obj finished')
        c.sort()
        print(b,c)
        if b == c:
            print('valid obj')
            a += 1
        c.clear()
print('obj finished')
c.sort()
print(b,c)
if b == c:
    print('valid obj')
    a += 1
print(a)
