import sys, math

case = int(sys.stdin.readline())
class_list=[int(i) for i in sys.stdin.readline().split()]
A,B=[int(i) for i in sys.stdin.readline().split()]
result =0
for i in range(case):
    if class_list[i]>=A:
        result=result+1+math.ceil((class_list[i]-A)/B)
    else:
        result+=1
        
print(result)