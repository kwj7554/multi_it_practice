import sys

case= int(sys.stdin.readline())
result={}
for i in range(case):
    [name, now]=sys.stdin.readline().rstrip().split(" ")
    if now == "enter":
        result[name]= true
    else:
        del result[name]

answer=sorted(result.keys(),reverse=True)

for j in range(len(answer)):
    print(answer[j])