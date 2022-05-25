import math

from campus.songdo import NodeSongdo as do
from campus.sinchon import NodeSinchon as ch

cons1 = 30 #상대적 거리인 length를 실제 거리로 바꿔주는 상수
cons2 = 1.5 #기울기에 따라 부가적으로 걸리는 시간을 고려하여 곱해주는 상수
complete=[]

def time(nodepoint): #노드에서 다음 노드로 갈 때의 거리와 높이를 시간으로 변환해주는 함수
    time=math.sqrt(pow(nodepoint[1],2)+pow((nodepoint[2]+1)*cons1,2))*(cons2*(nodepoint[2]+1))
    nodepoint[1]=time
    nodepoint[2]=0

def findmin(node): #현재 노드에서 다음 노드로 갈 때, 다음 노드들 중 걸리는 시간 중 최소 시간을 구하는 함수, 반환값: node이름
    mintime=-1 #mintime과 idx 초기화
    next_node=[]
    for j in node: #현재에서 갈 수 있는 다음 노드들이 무엇인지 리스트로 수합
        next_node.append(j[0])

    for i in next_node: #nodes=[[a,100],[b,20],[c,300]]

        if mintime==-1:
            min_name=i
            mintime = do[i][1]

        else:

            if do[i][1]<mintime or do[i][1]!=-1: #갈 수 있는 노드들 중에서, 시간이 가장 짧은 노드 발견
                mintime=do[i][1]
                min_name=i

    return min_name

def search(stops, end, way, tim=0): #전체 소요 시간을 구하는 함수


    if stops==end:
        return way, int(tim)

    for i in do[stops][2]: #time을 통해 시간으로 모두 변환/ i는 [a,100]형식
        time(i)

    for j in do[stops][2]: #갈 수 있는 다음 노드들(do[stops][2])을 전체 딕셔너리에서 찾아본 후, 걸리는 시간이 초기값 -1이면 지금 값으로 갱신
        if do[j[0]][1]==-1:
            do[j[0]][1]=j[1]

    if do[stops][1]>tim or do[stops][1]==-1: #갈 수 있는 다음 노드들(do[stops][2])을 리스트에서 찾아본 후, 걸리는 시간이 tim 보다 길면, 시간을 지금의 시간으로 갱신 후, 지금의 루트를 리스트에 추가
        do[stops][1]=tim
        way.append(stops)

    next=findmin(do[stops][2])
    print("next= ", next)
    search(next,end,way,tim+do[next][1])

way=[]
print(search('DormE','DormF',way))

