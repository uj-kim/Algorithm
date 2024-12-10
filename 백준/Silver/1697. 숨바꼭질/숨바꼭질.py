'''
[문제분석]
1. 수빈이
    - 현재 위치 N
    - 걷거나 순간이동 가능 (1초)
    - 걷기 : X-1, X+1
    - 순간이동 2X
2. 동생 : 현재 위치 K
3. 구해야 하는 것 : 수빈이가 동생을 찾을 수 있는 가장 빠른 시간
4. 입력 : N, K (공백 구분)
5. 출력 : 수빈이가 동생을 찾는 가장 빠른 시간
[문제해결과정]
1. 최단 경로(bfs 문제)
'''
import sys
from collections import deque

input = sys.stdin.readline

#입력 처리
N, K = map(int, input().split())

visited = set()


#bfs
#큐 초기화
queue = deque([(N, 0)])
visited.add(N)

while queue:
    cur, t = queue.popleft()
    if cur == K:
        print(t)
        
    for nx in (cur+1, cur-1, cur*2):
        if 0 <= nx <= 100000 and nx not in visited:
            visited.add(nx)
            queue.append((nx, t + 1))
            
