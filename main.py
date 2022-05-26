
# campus 폴더의 하위 항목인 songdo.py 파일과 sinchon.py 파일을 모듈로 임포트합니다.
from campus.songdo import NodeSongdo as So_
from campus.sinchon import NodeSinchon as Si_

print(Song_do)
print(Sin_chon)

def search(dir, stops, end, time=0):
    if So_[stops][0] > time:
        station[stops][0] = time
        dir.append(stops)
    else:
        return '취소'
    if stops == end:
        print(time)
        print(dir)
        return '도착'

    for i in station[stops][i]:
        trans = 0 if Line == i[1] else 5
        search(list(dir), i[0], end, i[1], i[2]+trans+time)

search([], '부평', '구로', line['수인선'])