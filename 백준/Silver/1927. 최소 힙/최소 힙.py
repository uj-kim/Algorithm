#2W_4일차_2번문제: 최소 힙
'''
[문제분석]
- 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램 작성
1. 배열에 자연수 X 삽입
2. 처음에 비어있는 배열에서 프로그램 시작

- 입력 
    1. 첫째 줄 : 연산의 개수 N
    2. 2 ~ N줄: 정수 X
                - 자연수 X => 배열에 X값 추가
                - 0 => 배열 최솟값 출력 후 제거
- 출력
    - 입력값 0에 대한 결과물만 출력.
    - 배열이 비어있는 경우 0 출력

[문제 해결 과정]
0. import heapq
1. 연산의 개수 N 입력 받기 int(input())
2. 최솟값을 구할 배열 min_heap = []
3. for _ in range(N), X = int(input()) -> X값 입력 받기
4. X값을 min_heap에 heappush해서 추가(X>0)
5. X == 0 인 경우, print(heapq.heappop(min_heap))
'''
#코드
import sys
import heapq

N = int(sys.stdin.readline())
min_heap = []

for _ in range(N):
    X = int(sys.stdin.readline())
    if X == 0:
        print(0 if not min_heap else heapq.heappop(min_heap))
        #if중첩이 아니라 예외처리로도 풀 수 있음
        # try :
        #   print(heapq.heappop(min_heap))
        # except IndexError:
        #   print(0)
    else:
        heapq.heappush(min_heap,X)

