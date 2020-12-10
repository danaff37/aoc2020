import sys
from parse import parse

valid=0

for line in sys.stdin:
    res=parse("{low:d}-{high:d} {char}: {pw}", line)
    if res['low'] <= res['pw'].count(res['char']) <= res['high']:
        valid += 1

print(valid)
