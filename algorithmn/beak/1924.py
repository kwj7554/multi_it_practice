import sys

[month,date]= [int(i) for i in sys.stdin.readline().split()]

for i in range(1,month):
    if i in [1,3,5,7,8,10,12]:
        date += 31
    elif i in [4,6,9,11] :
        date +=30
    else:
        date +=28
        
answer=date%7
if answer ==0:
    print("SUN")
elif answer == 1:
    print("MON")
elif answer == 2:
    print("TUE")
elif answer == 3:
    print ("WED")
elif answer == 4:
    print("THU")
elif answer == 5:
    print("FRI")
elif answer == 6:
    print("SAT")


    