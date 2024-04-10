import sys

case = int(sys.stdin.readline())
num_set=[]
for _ in range(case):
    num_set.append([int(i) for i in sys.stdin.readline().split()])
    
num_set.sort(key= lambda x:(x[0],x[1]))
for i in num_set:
    print(*i)