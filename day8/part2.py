import sys
import re

def test(insts):
    vis = [0] * len(insts)
    acc = 0
    lnum = 0
    while lnum < len(insts):
        vis[lnum] += 1
        if vis[lnum] > 1:
            break;
        if insts[lnum][0] == ('nop'):
            lnum += 1
        elif insts[lnum][0] == ('acc'):
            acc += int(insts[lnum][1])
            lnum += 1
        elif insts[lnum][0] == ('jmp'):
            lnum += int(insts[lnum][1])
    return (2 not in vis),acc

insts=[]
for line in sys.stdin:
    m = re.match(r'(acc|nop|jmp) ((-|\+)[0-9]+)',line.strip())
    insts.append([m.groups()[0],int(m.groups()[1])])

ch = 0
lis = [i[0] for i in insts[ch:]]
acc = 0
while 'jmp' in lis:
    ch += lis.index('jmp') + 1
    print('jmp',ch)
    insts[ch][0] = 'nop'
    r,a = test(insts)
    insts[ch][0] = 'jmp'
    if r:
        acc = a
        break
    lis = [i[0] for i in insts[ch+1:]]
ch = 0
if acc == 0:
    while 'nop' in lis:
        ch += lis.index('nop') + 1
        print('nop',ch)
        insts[ch][0] = 'jmp'
        r,a = test(insts)
        insts[ch][0] = 'nop'
        if r:
            acc = a
            break
        lis = [i[0] for i in insts[ch+1:]]
print(acc)

