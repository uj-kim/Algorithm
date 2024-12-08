#3W_4일차_1번문제 : DFS
'''
[문제분석]
- N개의 정점, M개의 간선의 무방향 그래프
- 1 ~ N번 정점 번호, 모든 간선 가중치 1
- 정점 R에서 시작. DFS로 노드 방문
- 방문 순서 출력

def dfs(V, E, R):
    visted[R] = "YES"
    for i in R:
        if visited[i]== "NO":
            dfs(V, E, i)

- 입력
    1. 정점 수 N, 간선 수 M, 시작정점 R(공백 구분)
    2. M개 줄 : 간선 정보 u v
- 출력
    1 ~ N개 줄 : i번째 줄 정점 i의 방문순서 출력
    (시작정점 방문순서는 1, 시작정점에서 방문할 수 없는 경우 0)

[문제 해결 과정]
dfs하면 됨
- 입력 (M+1줄)
    1. N M R => map(int,input().split())
    2. u v 
- 출력(N줄)
    - for i in range (N):
        정점 i의 방문순서

'''
#코드
#dfs 함수
# def dfs(V, E, R):
#     visited[R} = "YES"
#     for i in R:
#         if visited[i] == "NO":
#             dfs(V, E, i)

#입력값
import sys

def dfs(N, M, R):
    visited = [0]*(N+1)
    stack = [R]
    order = 1

    while stack:
        current = stack.pop()

        if visited[current] == 0:
            visited[current] = order
            order += 1

        for x in sorted(graph[current], reverse = True):
            if visited[x] == 0:
                stack.append(x)
    
    for i in range(1, N+1):
        print(visited[i])


N, M, R = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, N+1)}

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)


dfs(N, M, R)