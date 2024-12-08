import sys
from collections import deque

input = sys.stdin.readline

def bfs(N, R):
    queue = deque([R])
    visited[R] = 1  # 시작 정점 방문
    order = 2       # 방문 순서 시작

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if not visited[neighbor]:  # 방문하지 않은 정점만 처리
                queue.append(neighbor)
                visited[neighbor] = order
                order += 1

# 입력 처리
N, M, R = map(int, input().split())
visited = [0] * (N + 1)  # 방문 순서 기록
graph = [[] for _ in range(N + 1)]  # 인접 리스트

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 그래프 정렬 (한 번만 수행)
for i in range(1, N + 1):
    graph[i].sort()

# BFS 실행
bfs(N, R)

# 방문 순서 출력
for i in visited[1:]:
    print(i)
