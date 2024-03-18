import sys
N,case=[int(i) for i in sys.stdin.readline().split()]

Num = [int(i) for i in sys.stdin.readline().split()]
sum_Num=[0]
total=0

for i in range(len(Num)):
    total += Num[i]
    sum_Num.append(total)
    


for _ in range(case):
    start,end=[int(j) for j in sys.stdin.readline().split()]
    result = (sum_Num[end]-sum_Num[start-1])
    print(result)
    