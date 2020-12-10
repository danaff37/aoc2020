import sys

maxid=0
mincol=0
maxcol=7
minrow=0
maxrow=127
for line in sys.stdin:
    for i in range(0,7):
        diff = (maxrow - minrow) // 2 + 1   
        if line[i] == 'B': minrow = diff + minrow
        if line[i] == 'F': maxrow = maxrow - diff
    for i in range(7,10):
        diff = (maxcol - mincol) // 2 + 1
        if line[i] == 'R': mincol = diff + mincol
        if line[i] == 'L': maxcol = maxcol - diff
    id=maxrow*8+maxcol
    if maxid < id: maxid=id
    mincol=0
    maxcol=7
    minrow=0
    maxrow=127
print(maxid)
