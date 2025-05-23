"""
======================================================
* 문제  
  현재 형택구에 나온 국회의원 후보는 N명이다.
  다솜이는 이 기계를 이용해서 그 마을의 주민 M명의 마음을 모두 읽었다.

  다솜이는 기호 1번이다.
  다솜이는 사람들의 마음을 읽어서 자신을 찍지 않으려는
  사람을 돈으로 매수해서 국회의원에 당선이 되게 하려고 한다.

  른 모든 사람의 득표수 보다 많은 득표수를 가질 때,
  그 사람이 국회의원에 당선된다.

  예를 들어서, 마음을 읽은 결과
    기호 1번이 5표, << 다솜이가 당선을 당하고 싶데요.
    기호 2번이 7표,
    기호 3번이 7표 라고 한다면,
    다솜이는 2번 후보를 찍으려고
    하던 사람 1명과, 3번 후보를 찍으려고 하던 사람 1명을 돈으로 매수하면,
    국회의원에 당선이 된다.

* 입력
  첫 줄은 후보의 수 N <-int
  다음 줄은 기호 1부터 N까지의 후보중 찍으려는 표 수. <- int

  N은 50보다 작거나 같다 (자연수) 
  득표수는 100보다 작거나 같다 (자연수)

* 출력
  첫째 줄에 다솜이가 매수해야 하는 사람의 최솟값을 출력한다. 최대 heap을 쓰면 될 것 같습니다.!

* 예제 입력

* 예제 출력
======================================================

* 문제 분석 

* 의사 결정 

* 코드 구현
"""

import sys
import heapq

input = sys.stdin.readline

# 후보 수 N 
n = int(input())

# # 다른 후보자들 의 득표 수. # 최대 힙 
others = [] 
# # 기호 1번이 받을 표 
dasom = int(input()) 

# for 문으로 나머지 후보들의 득표 수를 입력 받기
# others = [int(input()) for _ in range(n - 1)] # others [ 1, 2 ]

for i in range(n-1):
  x = int(input())
  heapq.heappush(others, -x)

# 매수할 사람들의 수
cnt = 0

# 큰 득표수를 가진 후보를 하나씩 매수한다. while 문을 써서.
"""
?음수를 변수로 다시 풀어서, heappop을해서 원래 값으로 

? 조건문을 사용해서 원래 값이 다솜이보다 득표 수가 많은 후보가 있으면,
원래 값에 한 표를 매수해서 다솜이에게 추가한다.
그리고 다솜이의 득표 수를 증가하고, 매수한 사람의 수를 1 증가한다. 
그리고 다시 우선순위 큐에 넣는 방식을 사용해 조건문이 아니면 
더 이상 매수할 필요가 없으므로 반복문을 종료한다. 

print(매수한 사람. )

"""
# others에 값이 있으면 무한 루프 실행. 없으면 실행 종료.
while others: 
  # 최대값 을 heappop()을 통해 원래 값으로 
  most_get = -heapq.heappop(others)
  # 
  if most_get >= dasom: 
    most_get -= 1
    cnt += 1
    dasom += 1
    # 재정렬 + 넣어줌 
    heapq.heappush(others, -most_get)
  else : 
    break

print(cnt)
    
  
