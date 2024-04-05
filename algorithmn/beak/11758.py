import sys

p1= [int(i) for i in sys.stdin.readline().split()]
p2= [int(i) for i in sys.stdin.readline().split()]
p3= [int(i) for i in sys.stdin.readline().split()]

def ccw(p1 ,p2, p3):
    return (p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1])-(p1[1]*p2[0]+p2[1]*p3[0]+p3[1]*p1[0])

if ccw(p1,p2,p3)>0:
    print(-1)
elif ccw(p1,p2,p3) ==0:
    print(0)
else :
    print(1)
    
