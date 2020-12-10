import sys

found = []
sums = [0]
a = [0]

def permutate(j,b):
#     print(j,len(a),len(b))
    if j == len(a)-1:
#         if b not in found:
#         print('adding',b)
#             found.append(b)
        sums[0] += 1
        return
    for i in range(j+1,j+5):
        if i >= len(a): break
#         if i >= 10:
#             print(a[i+1],a[i])
        if a[i] - b[len(b)-1] <= 3:
            b.append(a[i])
            permutate(i,b)
            b.pop(len(b)-1)    
        else:
            break

for line in sys.stdin:
    a.append(int(line))
a.sort()
for i in range(1,4):
    if a[i] > 3: break
    print('running',i)
    b=[a[i]]
    if a[i+1] - a[i] > 3: continue
    permutate(i,b)
# print(len(found))
print(sums)
