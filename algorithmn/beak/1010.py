import sys

def calc(M,N):
    number =0
    calc= 1
    while number != N:
        calc=calc*M
        number +=1
        M-=1
    result=1
    for i in range(1,N+1):
        result*=i
    return calc/result

case = int(sys.stdin.readline())
for i in range(case):
    N,M=[int(j) for j in sys.stdin.readline().split()]
    print(int(calc(M,N)))
    