#2W_4일차_3번문제 :
'''
[요구사항]
- 산타는 세계 곳곳의 거점을 방문하여 선물을 충전할 예정
- 착한아이들을 만날 때마다 자신이 들고 있는 가장 가치가 큰 선물을 하나씩 선물할 것임
- 차례대로 방문한 아이들과 거점의 정보가 주어졌을 때,
- 아이들이 준 선물들의 가치들을 출력
- 아이들에게 줄 선물이 없다면 -1 출력

- 입력
    1. 첫 번째 줄 : 아이들과 거점지를 방문한 횟수 n
    2. 2 ~ n줄 
        - a값이 들어오고 
        - a개의 숫자 : a개의 선물 충전(== 선물들의 가치가 나열되어 있는 형태)
        - a == 0 => 거점지가 아닌 아이들을 만난 것

- 출력
    a가 0일 때마다, 아이들에게 준 선물의 가치를 출력
    - 줄 선물이 없다면 -1 출력.

[문제 해결 과정]
- import heapq
- 입력값 n : 아이들을 거점지를 방문한 횟수
- gift_list = []
- for _ in range(n): 거점을 돌 때마다
    center = int(input().split())
    a = center[0]
    center center[1]부터 a개까지의 요소를 돌면서
    gift_list에 heappush로 추가 (-x로, 최댓값 뽑아야하므로) 

- 선물을 주는 게 거점이 아닌 아이들을 만났을 때 인가?
- 그렇다면 if문으로 a == 0일때
- -heapq.heappop(gift_list) 해서 최대 가치의 선물을 빼주기
- gift_list가 0일경우 -1출력

'''
#코드
import heapq

n = int(input())
gift_list = []

for _ in range(n):
    center = list(map(int,input().split()))
    a = center[0]
    
    if a == 0:
        
        if not gift_list:
            print(-1)

        else:
            print(-heapq.heappop(gift_list))

    else:
        for x in center[1:]:
            heapq.heappush(gift_list, -x)

    