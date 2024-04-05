import sys

case = int(sys.stdin.readline())

num_set=(i for i in sys.stdin.readline().split())

my_card = int(sys.stdin.readline())

my_card_list=sys.stdin.readline().split()
result=[]
for i in range(my_card):
    result.append(1 if my_card_list[i] in num_set else 0 )

print(*result)


# import sys

# card= int(sys.stdin.readline())
# card_list= set(sys.stdin.readline().split())

# test= int(sys.stdin.readline())
# test_list = sys.stdin.readline().split()
# result=[]
# for i in test_list:
#     if i in card_list:
#         result.append(1)
#     else:
#         result.append(0)

# print(*result)
#