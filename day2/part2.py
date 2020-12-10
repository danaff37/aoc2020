import sys
from parse import parse

valid=0

for line in sys.stdin:
    res=parse("{low:d}-{high:d} {char}: {pw}", line)
    if (res['pw'][res['low']-1] == res['char']) ^ (res['pw'][res['high']-1] == res['char']):
        valid += 1

print(valid)
