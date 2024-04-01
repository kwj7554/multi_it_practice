import sys

case= int(sys.stdin.readline())
a_list=[int(i) for i in sys.stdin.readline().split()]
b_list=[int(i) for i in sys.stdin.readline().split()]

# a_list.sort(reverse=True)
# b_list.sort()
# result=0
# for i in range(case):
#     result+=a_list[i]*b_list[i]

result=0
for i in range(case):
    result+=min(a_list)*max(b_list)
    a_list.pop(a_list.index(min(a_list)))
    b_list.pop(b_list.index(max(b_list)))
print(result)