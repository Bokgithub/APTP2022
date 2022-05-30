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