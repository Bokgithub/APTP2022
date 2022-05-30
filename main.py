
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