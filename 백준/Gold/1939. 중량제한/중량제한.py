#4번문제
'''
[문제]
- N(2<= N <= 10000)개의 섬으로 이루어진 나라.
- 몇 개의 섬에만 다리가 설치되어있음(인접노드)
- 다리마다 중량제한이 있음(가중치)
- 가중치를 초과하면 안 됨
- 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하라

[입력]
    1. 첫째 줄 : N, M(공백구분, 섬개수, 다리개수)
    2. M개의 줄 : 다리의 정보 A, B, C
        => A섬-B섬 연결 다리 가중치가 C
    (다리는 여러개가 있을 수 있음. 양방향)
    3. 마지막줄 : 공장이 위치한 두 섬의 번호(공백 구분)

[출력]
    공장 -> 공장 : 최대중량

[문제 해결 과정]
시작노드 -> 목표노드 : 최대 중량
가능한 중량을 이진탐색으로 범위를 좁혀나가면서 탐색할 예정
'''
#코드
import sys
from collections import deque

input = sys.stdin.readline

# BFS 탐색
def bfs(start, end, min_limit):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        cur = queue.popleft()

        if cur == end:
            return True

        for node, weight in graph[cur]:
            if not visited[node] and weight >= min_limit:
                queue.append(node)
                visited[node] = True

    return False

# 입력 처리 및 그래프 생성
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
max_weight = 0  # 최대 가중치 추적

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
    max_weight = max(max_weight, C)  # 최대 가중치 갱신

start, end = map(int, input().split())

# 이진 탐색
lowest, highest = 1, max_weight
result = 0

while lowest <= highest:
    mid = (lowest + highest) // 2

    if bfs(start, end, mid):
        result = mid  # 가능한 최대 중량 갱신
        lowest = mid + 1  # 더 큰 중량 탐색
    else:
        highest = mid - 1  # 더 작은 중량 탐색

print(result)
