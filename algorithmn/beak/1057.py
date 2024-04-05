import sys

[num,a,b]=[int(i) for i in sys.stdin.readline().split()]

def calc(num):
    if num == 1:
        return 1
    elif num%2==0:
        return num//2
    else:
        return num//2+1

result = 0
while a!=b:
    a=calc(a)
    b=calc(b)
    result +=1

print(result)
