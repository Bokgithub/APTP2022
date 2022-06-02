import math
import heapq
from campus.songdo import NodeSongdo as Song_
from campus.sinchon import NodeSinchon as Sin_

cons1 = 1.1 #기울기에 따라 부가적으로 걸리는 시간을 고려하여 곱해주는 상수
cons2 = 0.9
cons3= 0.015 #상대적 거리인 length를 실제 거리로 바꿔주는 상수


def Time(do): #노드에서 다음 노드로 갈 때의 거리와 높이를 시간으로 변환해주는 함수
    for key, value in nodes.items():
        for next in value[2]:
            if next[2]>0:
                time=(next[1] * cons3) * next[2] * cons1
            elif next[2]<0:
                time=(next[1] * cons3) * (- next[2]) * cons2
            else:
                time=(next[1] * cons3)
            next[1]=time
            next[2]=0
            '''time = math.sqrt(pow(next[1]* 0.015, 2) + pow((next[2] + 1) * cons1, 2)) * (cons2 * (next[2] + 1))
            next[1]=time
            next[2]=0

def FindMin(node): #현재 노드에서 다음 노드로 갈 때, 다음 노드들 중 걸리는 시간 중 최소 시간을 구하는 함수, 반환값: node이름
    mintime=math.inf  #mintime과 idx 초기화
    min_name=''
    for key, value in do: #nodes=[[a,100],[b,20],[c,300]]
        if value[1] <= mintime:
            min_name = key
            mintime = value[1]
    return min_name, mintime
'''

def SearchPathTime(stops, end, tim,done=[], queue=[], way={}): #전체 소요 시간을 구하는 함수


    if stops==end: #도착지라면 지금까지의 거리와 시간을 반환함.
        dir= way[stops]
        return dir, tim

    for next in nodes[stops][2]: #갈 수 있는 다음 노드들(do[stops][2])에 대해 현재 경로를 통해 가는 시간이 더 짧다면, 시간과 경로 갱신
        height=next[2]
        if height==0:
            tim_=next[1]
        elif height>0:
            tim_=next[1]+next[2]*cons1
        elif height< 0:
            tim_=next[1]+next[2]*cons2

        tim+=tim_



        if tim < nodes[next[0]][1]:
            nodes[next[0]][1] = tim

            if stops in way: #way라는 딕셔너리에, 가장 짧은 경로를 갱신함. 이때의 경로는 현재의 stops까지 오는 경로에 stops를 추가한 것임.
                dir=way[stops]
                dir.append(stops)
                way[next[0]] = dir

            else:
                way[next[0]]=[stops]


            if (next[0] in done) == False:
                heapq.heappush(queue, [tim, next[0]]) #힙을 이용하여 다음 역들을 넣어 다음 탐색 경로를 만듦.
                done.append(next[0]) #done은 이미 지나온 경로를 체크하는 함수

    next=heapq.heappop(queue) #heapq.pop을 통해 남은 경로들 중 가장 짧은 시간을 탐색함.
    SearchPathTime(next[1], end,  next[0],done, queue, way)


    return way[end], tim


way={}
tim=0
done=[]
queue=[]




#입출력
print("사용할 위치를 고르세요.")
print("1 : 신촌캠퍼스  2 : 국제캠퍼스")
Map =int( input("숫자를 입력하세요 : "))

if Map==1:
    nodes=Song_
elif Map==2:
    nodes=Sin_
else:
 print("잘못 입력하셨습니다")

way, time= SearchPathTime('Yplaza', 'YICfield',  tim,done, queue, way)
print('way = ',way)


# 개인별 보행 속력 입력 (성인의 평균 보행 속력=4.8km/h)
velocity=float(input("본인의 보행 속력를 입력하세요[km/h]: "))

# 최단경로의 가중치의 합을 기존의 코드를 통해 입력 받는다 = time
# 비례 상수 = d (sum*d= 총 이동거리[km])

d=0.001

# 전체 소요 시간 = T[h]
T=time*d/velocity

if(T <= 1/6):
    print("%.2f분 소요, 쉬는 시간 내에 도착 가능합니다." %(T*60))
else:
    recommend_velocity=sum*d/(1/6)
    print("평균 %.2fkm/h의 속력으로 달려야만 쉬는 시간 내에 도착 가능합니다." %(recommend_velocity))