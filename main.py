<<<<<<< HEAD

# campus 폴더의 하위 항목인 songdo.py 파일과 sinchon.py 파일을 모듈로 임포트합니다.
from campus.songdo import NodeSongdo as Song_
from campus.sinchon import NodeSinchon as Sin_

#print(Song_)
#print(Sin_)
print("사용할 위치를 고르세요.")
print("1 : 신촌캠퍼스  2 : 국제캠퍼스")
place = input("숫자를 입력하세요 : ")

load = []
t = []

#신촌캠퍼스
if place == 1:
    def search(dir, stops, end, time=0):
        if Sin_[stops][1] > time:
            Sin_[stops][1] = time
            dir.append(stops)
        else:
            return '취소'
        if stops == end:
            load.append(dir)
            t.append(time)
            load[t.index(min(t))]
            print(f'지나온 길 : {load[t.index(min(t))]}')
            print(f'걸린 시간 : {round(min(t), 1)} 분')
            return '도착'

        for i in Sin_[stops][2]:  # Song_[stops][2] = [['nodem', 57, 0], ['noden', 56, 0], ['nodes', 19, 0]] 요느낌
            if i[2] > 0:  # 오르막길->시간 더 걸림. 가중치 (i[2]*1.1)로 해봄. 상대높이가 24까지 있다해서
                search(list(dir), i[0], end, (i[1] * 0.015) * i[2] * 1.1 + time)  # i[0]은 'nodem', i[1] = 57(거리), i[2] = 0(높이) 의미
            elif i[2] < 0:  # 내리막길->시간 덜 걸림. 가중치 (-i[2]*0.9)로 해봄. 상대높이가 24까지 있다해서
                search(list(dir), i[0], end, (i[1] * 0.015) * (-i[2]) * 0.9 + time)
            else:  # 평지. 가중치 없음
                search(list(dir), i[0], end, (i[1] * 0.015) + time)


    # 사람 속도 = 1000m 15분 적용.-> 1m 0.015분
    # 여기에 상대 고도 고려해야함.

#송도캠퍼스
else:
    def search(dir, stops, end, time=0):
        if Song_[stops][1] > time:
            Song_[stops][1] = time
            dir.append(stops)
        else:
            return '취소'
        if stops == end:
            load.append(dir)
            t.append(time)
            load[t.index(min(t))]
            print(f'지나온 길 : {load[t.index(min(t))]}')
            print(f'걸린 시간 : {round(min(t), 1)} 분')
            print(t, load)
            return '도착'

        for i in Song_[stops][2]:  # Song_[stops][2] = [['nodem', 57, 0], ['noden', 56, 0], ['nodes', 19, 0]] 요느낌
            if i[2] > 0:  # 오르막길->시간 더 걸림. 가중치 (i[2]*1.1)로 해봄. 상대높이가 24까지 있다해서
                search(list(dir), i[0], end,
                       (i[1] * 0.015) * i[2] * 1.1 + time)  # i[0]은 'nodem', i[1] = 57(거리), i[2] = 0(높이) 의미
            elif i[2] < 0:  # 내리막길->시간 덜 걸림. 가중치 (-i[2]*0.9)로 해봄. 상대높이가 24까지 있다해서
                search(list(dir), i[0], end, (i[1] * 0.015) * (-i[2]) * 0.9 + time)
            else:  # 평지. 가중치 없음
                search(list(dir), i[0], end, (i[1] * 0.015) + time)


    # 사람 속도 = 1000m 15분 적용.-> 1m 0.015분
    # 여기에 상대 고도 고려해야함.


search([], 'Yplaza', 'YICfield')
search([], 'Yplaza', 'gatea')
search([], 'Futsal', 'gatea')
=======
# 최단경로의 가중치의 합을 기존의 코드를 통해 입력 받는다 = sum
# 비례 상수 = d (sum*d= 총 이동거리[km])
sum=400
d=0.001

# 개인별 보행 속력 입력 (성인의 평균 보행 속력=4.8km/h)
velocity=float(input("본인의 보행 속력를 입력하세요[km/h]: "))

# 전체 소요 시간 = T[h]
T=sum*d/velocity

if(T <= 1/6):
    print("%.2f분 소요, 쉬는 시간 내에 도착 가능합니다." %(T*60))
else:
    recommend_velocity=sum*d/(1/6)
    print("평균 %.2fkm/h의 속력으로 달려야만 쉬는 시간 내에 도착 가능합니다." %(recommend_velocity))
>>>>>>> origin/visualize
