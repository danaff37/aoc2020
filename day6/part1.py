import sys

a=[0]*26
b=0
for l in sys.stdin:
    if l.strip():
        for c in l.strip():
            a[int(c,36)-10]=1
    else:
        b+=a.count(1)
        a=[0]*26
b+=a.count(1)
print(b)
