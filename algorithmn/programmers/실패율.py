def solution(N, stages):
    humen=[0]*(N+2)
    for i in stages:
        humen[i]+=1
    humen_num=len(stages)
    result=[]
    for i in range(len(humen)):
        if i>=1 and i<=N:
            humen_num-=humen[i-1]
            if humen[i]==0 and humen_num==0:
                result.append(0)
            else:
                result.append(humen[i]/humen_num)
            
    answer = [i for i in enumerate(result)]
    last_answer = [i+1 for i,_ in sorted(answer,key= lambda x: -x[1])]
    return last_answer

print(solution(5,[2,1,2,6,2,4,3,3]))