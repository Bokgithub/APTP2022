class Dijkstra(object):
# campus 폴더의 하위 항목인 songdo.py 파일과 sinchon.py 파일을 모듈로 임포트합니다.
from src.campus.songdo import NodeSongdo as Song_
from src.campus.sinchon import NodeSinchon as Sin_
def __init__(self):
        self.load = []
        self.t = []
        self.dir = []

def search(self, stops, end, time=0):
        # Ui_MainWindow에서 campus 정보를 받아옵니다.
        if Ui_MainWindow.SinchonCampus.isChecked() == True:
        cam = self.Sin_
        if Ui_MainWindow.SongdoCampus.isChecked() == True:
        cam = self.Song_
        
        # Ui_MainWindow에서 속도 정보를 받아옵니다.
        if Ui_MainWindow.HowSpeed() != None:
        speed = Ui_MainWindow.HowSpeed()

        if cam[stops][1] > time:
        cam[stops][1] = time
        self.dir.append(stops)
        else:
        return None
        if stops == end:
        self.load.append(self.dir)
        self.t.append(time)
        self.load[self.t.index(min(self.t))]
        Way = f'지나온 길 : {self.load[self.t.index(min(self.t))]}'
        Usedtime = f'걸린 시간 : {round(min(self.t), 1)} 분'
        return Way, Usedtime

        for i in cam[stops][2]:  # Song_[stops][2] = [['nodem', 57, 0], ['noden', 56, 0], ['nodes', 19, 0]] 요느낌
        minutes = (i[1] * speed) * i[2]
        slope = 1.1 if i[2] > 0 else 0.9 if i[2] < 0 else 1.0
        # 오르막길->시간 더 걸림. 가중치 (i[2]*1.1)로 해봄. 상대높이가 24까지 있다해서
        # 내리막길->시간 덜 걸림. 가중치 (i[2]*0.9)로 해봄. 상대높이가 24까지 있다해서
        # 평지. 가중치 없음
        gotime = minutes * slope
        self.search(list(dir), i[0], end, gotime + time)

        # 사람 속도 = 1000m 15분 적용.-> 1m 0.015분
        # speed == 2.5 km/h -> 1m 0.024분
        # speed == 4.5 km/h -> 1m 0.013분
        # speed == 7.5 km/h -> 1m 0.008분
        # speed == Usain -> 1m 0.0016분
