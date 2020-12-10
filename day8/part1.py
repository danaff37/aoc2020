import sys

insts=[]
for line in sys.stdin:
    insts.append(line.strip())

vis=[0] * len(insts)
acc = 0
lnum = 0
while 2 not in vis:
    if vis[lnum] > 0:
        break;
    vis[lnum] += 1
    if insts[lnum].startswith('nop'):
        lnum += 1
    elif insts[lnum].startswith('acc'):
        acc += int(insts[lnum][4:])
        lnum += 1
    elif insts[lnum].startswith('jmp'):
        lnum += int(insts[lnum][4:])

print(acc)
