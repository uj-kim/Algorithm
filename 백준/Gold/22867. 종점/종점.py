#정보상인호석
#문제 해결 방법:
'''
[문제]
- 상황
    1. 주행이 끝난 버스들이 종점에 들어오는 상황
    2. 버스가 n대 -> 주차공간 n+@ 필요
    3. 버스 B out, 버스 A in
    4. 버스 시간표가 변경되어 "주차공간 개수 다시 계산" 필요
- 입력
    1. 들어오는 버스 개수 N
    2. ~ N개의 줄 : 버스 in시간 out시간
        - 형식 : HH:MM:SS.sss
        - in시간 < out시간

- 출력
    : 버스 차고지의 최소 공간 개수

[문제해결과정]
0. 문자열, 정렬, 우선순위큐?

1. 입력값 형변환
    - "HH:MM:SS.sss"로 받으니까 -> int로 바꿔서 편하게 활용해줄 예정
    - 파이선의 datetime 모듈 활용

2. 들어오는 시간(intime)을 기준으로 나가는 시간(outtime)을 heappush

3. intime이 heap의 [0]보다 적으면 outtime heappush
4. intime이 heap의 [0]보다 크면 outtime heappop하고
outtime heappush
5. 최종 heap길이 출력

- 필요 변수
    - N : int, input받을 버스 정보
    - intime, outtime : str->int, 버스 들어오는/나가는 시간
    - garage : heap, 버스 차고지

    
- 활용 메서드 
    1. datetime
    2. heapq

'''
#코드
import sys
import heapq
from datetime import datetime

input = sys.stdin.readline

# 시간을 초 단위로 변환
def int_time(x):
    change_x = datetime.strptime(x, "%H:%M:%S.%f")
    nx = (change_x.hour * 3600 + change_x.minute * 60 + change_x.second) * 1000 + (change_x.microsecond // 1000)
    return int(nx)

# 우선순위 큐
garage = []
heap=[]
n = int(input())  # 버스 개수 입력

#입력값 처리
for _ in range(n):
    intime, outtime = map(str, input().split())
    intime = int_time(intime)
    outtime = int_time(outtime)

    garage.append((intime, outtime))

garage.sort()
heapq.heappush(heap, garage[0][1])

for i in range(1, n):
    if garage[i][0] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, garage[i][1])

print(len(heap))