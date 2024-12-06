#3W_3일차_3번문제
'''
[문제분석]
- 고정된 크기 (5X5)의 숫자판
- 각 칸에는 숫자 0 ~ 9가 적혀 있음
- 숫자판의 임의의 위치에서 네 방향으로 다섯 번 이동
- 각 칸에 적혀 있는 숫자를 차례로 붙여서 6자리 수 생성
- 중복 허용, 0으로 시작 가능
- 입력 : 5개의 정수를 5개의 줄에 걸쳐서 입력받음(공백 구분)
- 출력 : 만들 수 있는 수들의 개수(6자리)
[문제 해결 과정]
1. 모든 노드를 탐색하면서 6자리를 만들어서 조합
2. 모든 노드 탐색 => dfs
3. 6자리 => 조건
4. 방문했던 노드 재방문 가능 -> visited 필요 없음
5. 같은 6자리는 안 됨 => 결과는 set()에 넣어줌
6. 인접한 네 방향으로 이동 => 상(0,1), 하(0, -1), 좌(-1,0), 우(1,0) directions활용
7. 숫자가 아니라 문자로 취급해서 풀어줄 예정
'''
#코드
board = [input().split() for _ in range(5)]

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
result = set()

#모든 노드 방문
for i in range(5):
    for j in range(5):
        stack = [(i, j , board[i][j])]
        #dfs 시작
        while stack:
            x, y, num = stack.pop()

            if len(num) == 6:
                result.add(num)
            else:
                 for dx, dy in directions:
                     nx, ny = x+dx, y+dy
                     if 0 <= nx <5 and 0 <= ny < 5:
                         stack.append((nx, ny, num + board[nx][ny]))

print(len(result))