import sys
from collections import deque
[case, k]=[int(i) for i in sys.stdin.readline().split()]
result=deque([])

for i in range(case):
    result.append(i+1)

answer=[]
print(result)
for i in range(case):
    result.rotate(-k)
    x= result.pop()
    answer.append(str(x))


print("<"+", ".join(answer)+">")

# 인덱스가 계속 커지지만 리스트의 길이보다 커지면 그만큼 다시 0번부터 시작해서 찾았으면 좋겠다.

