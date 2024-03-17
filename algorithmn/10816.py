import sys, collections

card_num=int(sys.stdin.readline())

card_list=sys.stdin.readline().split()
case=int(sys.stdin.readline())
case_list=sys.stdin.readline().split()

num_dict=collections.Counter(card_list)
result =[]
for j in case_list:
    result.append(num_dict[j])
    
print(*result)   