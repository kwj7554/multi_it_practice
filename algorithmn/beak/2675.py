import sys

case= int(sys.stdin.readline())

for _ in range(case):
    num,string=[j for j in sys.stdin.readline().split()]
    num=int(num)
    result=[i*num for i in string]
    print("".join(result))

