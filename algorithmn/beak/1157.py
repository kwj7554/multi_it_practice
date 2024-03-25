import sys, collections

a=sys.stdin.readline().rstrip().lower()

b= collections.Counter(a).most_common()

if len(b)>1 and b[0][1]==b[1][1]:
    print("?")
else:
    print(b[0][0].upper())