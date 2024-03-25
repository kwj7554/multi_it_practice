import math
def solution(fees,records):
    re_records=[i.split(" ") for i in records]

    for i in range(len(re_records)):
        re_records[i][0]=[int(j) for j in re_records[i][0].split(":")]
        re_records[i][0]=re_records[i][0][0]*60+re_records[i][0][1]
        
    car_dict={}
    for i in re_records:
        if i[1] in car_dict:
            car_dict[i[1]].append(i[0])
        else:
            car_dict[i[1]]=[i[0]]
        
    car_num=sorted(car_dict.keys())

    for i in car_num:
        result=[]
        if len(car_dict[i])%2==1:
            car_dict[i].append(1439)
        start =0
        end=1
        for j in range(int(len(car_dict[i])/2)):
            time=car_dict[i][end]-car_dict[i][start]
            start+=2
            end+=2
            result.append(time)
        if sum(result)<=fees[0]:
            result=fees[1]
        else:
            result=fees[1]+math.ceil((sum(result)-fees[0])/fees[2])*fees[3]
        car_dict[i]=result
    answer=[]
    for i in car_num:
        answer.append(car_dict[i])
    
    return answer