import sys

a=[0]*26
b=0
q=0
for l in sys.stdin:
    if l.strip():
        for c in l.strip():
            a[int(c,36)-10]+=1
        q+=1
    else:
        b+=a.count(q)
        a=[0]*26
        q=0
b+=a.count(q)
print(b)
