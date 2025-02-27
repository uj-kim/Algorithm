#3W_5일차_1번문제
'''
[문제분석]
체스판 위에 나이트. 
나이트가 이동하려고 하는 칸까지 몇 번 움직여야할까?
- 입력
    1. 첫째 줄 : 테스트 케이스 개수 T
    2-1. 체스판 한 변의 길이 l (체스판 규격은 l x l)
    2-2. 나이트의 현재 위치(x좌표, y좌표)
    2-3. 나이트가 이동하려고 하는 칸(x좌표, y좌표)
- 출력 : 테스트케이스별 나이트의 최소 이동횟수

[문제 해결 과정]
0. 시작지점에서 목표지점까지 최소 이동횟수(최단경로와 유사) => bfs로 탐색해서 풀어야겠다
1. 입력
    - 테스트 케이스 T -> int(input())
    - T만큼 반복 => 첫째 줄 : 체스판 한 변의 길이 l
                =>둘째 줄 : 나이트의 현재 위치 -> x, y
                => 셋째 줄 : 나이트의 목적지 -> nx, ny
    - 이동 directions = [(-2, 1), (2, -1), (2, 1), (1, 2), (-2, -1), (-1, -2), (1, -2), (2, -1)]
visited = 0 -> 1
2. 탐색 (bfs)
3. 출력 
'''
#코딩
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
