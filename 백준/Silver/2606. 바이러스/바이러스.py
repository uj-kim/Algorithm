import sys
from collections import deque

input = sys.stdin.readline

computers = int(input())
pairs = int(input())
graph = [[] for _ in range(computers+1)]
result = set()
result.add(1)

for _ in range(pairs):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    queue = deque([x])
    while queue:
        computer = queue.popleft()

        for i in graph[computer]:
            if i not in result:
                result.add(i)
                queue.append(i)

bfs(1)

print(len(result)-1)
