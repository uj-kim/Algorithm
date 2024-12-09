#3W_5일차_2번문제
'''
[문제분석]
- 1 ~ N번까지의 도시, M개의 단방향 도로(도로의 거리는 1)
- 특정 도시 X에서 출발하여 도달할 수 있는 모든 도시 중에서 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램
- X에서 X로 가는 최단거리는 항상 0
- 입력
    1. 첫째 줄 : 도시의 개수 N, 도로의 개수 M, 거리정보 K, 출발도시의 번호 X
    2. ~ M개의 줄 : A B(공백구분, A -> B 단방향 도로)
- 출력
    1. X에서 출발해서 도달할 수 있는 도시 중에서 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력
    - 도달할 수 있는 도시 중에서 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1 출력

[문제 해결 과정]
- 입력
    1. 첫째 줄 (공백 구분)
        - N : 도시 수 (Node)
        - M : 도로 수 (Edge)
        - K : 거리 정보 (route edges)
        - X : 출발 도시 번호
        => N, M, K, X = map(int, input().split())
    2. ~ M개의 줄 (공백 구분)
        - A B : A -> B 로가는 Edge 나타냄
        => for _ in range(M):
            A, B = map(int, input().split())
- 탐색 (최단 경로 -> bfs)
- graph를 딕셔너리 형태로 담아주기
- 인접노드 탐색(X에서 시작)
- count 변수 0 만들어주고, popleft()해서 이동할 때 count += 1하는 식.
- K가 되면 result 배열(오름차순)에 담아주고 하나씩 출력
'''
#코드
import sys
from collections import deque

input = sys.stdin.readline

def bfs(N, M, K, X):
    queue = deque([X])
    
    while queue:
        cur = queue.popleft()

        for i in graph[cur]:
            if route[i] == -1:
                route[i] = route[cur] + 1
                queue.append(i)


N, M, K, X = map(int, input().split())

route = [-1] * (N + 1)
graph = [[] for _ in range(N+1)]
route[X] = 0

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B) #단방향

for i in range(1, N + 1):
    graph[i].sort()

bfs(N, M, K, X)

result = [i for i in range(1, N + 1) if route[i] == K]

if result:
    print('\n'.join(map(str, result)))
else:
    print(-1)