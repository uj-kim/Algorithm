import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
directions = [(-2, 1), (-2, -1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

for _ in range(T):
    l = int(input())
    x, y = map(int, input().split())
    nx, ny = map(int, input().split())

    # 시작점과 목표점이 같다면 0 출력
    if (x, y) == (nx, ny):
        print(0)
        continue

    # BFS 초기화
    board = [[-1] * l for _ in range(l)]  # 방문 확인 및 거리 기록
    queue = deque([(x, y)])
    board[x][y] = 0

    # BFS 탐색
    while queue:
        cx, cy = queue.popleft()

        for dx, dy in directions:
            rx, ry = cx + dx, cy + dy

            if 0 <= rx < l and 0 <= ry < l and board[rx][ry] == -1:  # 방문하지 않은 유효한 위치
                board[rx][ry] = board[cx][cy] + 1  # 이동 횟수 갱신
                if (rx, ry) == (nx, ny):  # 목표 위치에 도달하면 종료
                    print(board[rx][ry])
                    queue = deque()  # BFS 종료
                    break
                queue.append((rx, ry))
