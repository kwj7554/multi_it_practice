import sys

N,M = [int(i) for i in sys.stdin.readline().split()]
listen=[]
watch=[]
for i in range(N):
    listen.append(sys.stdin.readline().rstrip())
    
for j in range(M):
    watch.append(sys.stdin.readline().rstrip())

result = list(set(listen) & set(watch))
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])       
    