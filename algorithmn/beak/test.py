import sys, collections

a=sys.stdin.readline().rstrip().lower()

b= collections.Counter(a).most_common()

print(b[1])