import sys, heapq   

case =int(sys.stdin.readline())
heap=[]
for _ in range(case):
    num=int(sys.stdin.readline())
    if num==0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,(-num,num))
# heapq를 이용하다면 내부 로직에 의하여 정렬이 된다.
# append를 써도 상관없지만 시간과 오류가 일어나지 않기 위하여 
#  heapq를 쓸 떄는 heapq를 써서 넣고 빼자

