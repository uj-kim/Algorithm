'''
[문제 분석]
- 마법의 뿅망치
- 뿅망치에 맞은 사람의 키가 2분의 1로 줄어듦(마지노선 1)
- 뿅망치는 횟수 제한이 있기 때문에 가장 키가 큰 거인을 뿅뿅
- 목표 : 거인나라의 모든 거인이 센티보다 키가 작도록
- 입력
    1. 첫 번째 줄 : 센티를 제외한 거인나라의 인구수 N, 센티의 키 H_centi, 뿅망치 횟수 T (공백으로 구분)
    2. 2 ~ N번째 줄 : 각 거인의 키 H
- 출력 
    1. 거인나라의 모든 거인의 키 < 센티 => YES
    2. 마법의 뿅망치를 최소로 사용한 횟수
    or
    1. 거인 >= 센티 => NO
    2. 남은 거인 중 키가 가장 큰 거인의 키 출력

[문제 해결 과정]
1. 3개의 값을 입력을 받아야함
 => N, H_centi, T = map(int, input())
2. heapq 사용
3. 거인의 키를 넣을 giants 변수 => giants = []
 2. N(거인의 수)만큼 거인의 키 입력값 받기
=> for _ in range(N):
    거인의 키 입력받기 H = int(input())
    heapq.heappush(giants, -H)
4. 뿅망치 횟수만큼 최장신 거인의 키를 줄여야 하는 과정
 => for i in range(T):
    - 최장신 거인의 키 꺼내기 max_height = -heapq.heappop(giants)
    - max_heigt < H(센티의 키) :
        print("YES")
        print(i)
    - 그게 아니라면
    - 2분의 1로 줄여준 다음 다시 heap에 넣어주기
        half_height = max_height // 2
        heapq.heappush(giants, - half_height)

last_height = -heapq.heappop(giants)
if  last_height >= Hcn:
    print("NO")
    print ("last_height")
'''
#코드
import heapq
N, Hcn, T = map(int,input().split())
giants = []

for _ in range(N):
    H = int(input())
    heapq.heappush(giants, -H)

for i in range(T):
    max_height = -heapq.heappop(giants)
    
    if max_height < Hcn:
        heapq.heappush(giants, -max_height)  # 다시 힙에 넣어줌

        print("YES")
        print(i)
        break

    half_height = max(max_height // 2, 1)
    heapq.heappush(giants, -half_height)

# last_height = -heapq.heappop(giants)
# if last_height >= Hcn:
#     print("NO")
#     print(last_height)

else:
    if -giants[0] < Hcn:
        print("YES")
        print(T)
    else:
        print("NO")
        print(-giants[0])
    