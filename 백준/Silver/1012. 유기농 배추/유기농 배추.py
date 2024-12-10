#3번문제
'''
1. 테스트케이스(T)
    - 배추 가로 길이 M
    - 배추 세로 길이 N
    - 심은 배추 개수 K
    - 각 배추의 위치(x,y) <- K만큼
2. 배추 field의 크기 = M*N
3. visited = set()
4. directions = [(-1,0),(0,-1),(0,1),(1,0)]
4. 최소 흰지렁이의 개수 -> bfs탐색
5. 개수 count 변수
'''
#코드
import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    field[x][y] = 0
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < M and 0 <= ny < N and field[nx][ny] == 1:
                queue.append((nx, ny))
                field[nx][ny] = 0


T = int(input())
for _ in range(T):

    M, N, K = map(int, input().split())

    field = [[0]*N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1

    #인접노드 탐색
    count = 0
    for i in range(M):
        for j in range(N):
            if field[i][j] == 1:
                bfs(i, j)
                count += 1
    
    print(count)