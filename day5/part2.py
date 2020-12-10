import sys

a=[0]*(127*8+7+1)
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
    a[id]=1
    mincol=0
    maxcol=7
    minrow=0
    maxrow=127
for i in range(1,1023):
    if a[i]==0 and a[i-1]>0 and a[i+1]>0:
        print(i)
        break
