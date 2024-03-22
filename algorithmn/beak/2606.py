import sys

computer_num=int(sys.stdin.readline())
edjes_num = int(sys.stdin.readline())
tree=[[] for i in range(computer_num+1)]
for _ in range(edjes_num):
    m,c = [int(i) for i in sys.stdin.readline().split()]
    tree[m].append(c)
    tree[c].append(m)
result=[]    
def dfs(num):
    result.append(num)
    for i in tree[num]:
        if i not in result:
            dfs(i)
            
            
dfs(1)
print(len(result)-1)