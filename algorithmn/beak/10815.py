import sys

case = int(sys.stdin.readline())

num_set=(i for i in sys.stdin.readline().split())

my_card = int(sys.stdin.readline())

my_card_list= [i for i in sys.stdin.readline().split()]
result=[]
for i in range(my_card):
    result.append(1 if my_card_list[i] in num_set else 0 )

print(result)