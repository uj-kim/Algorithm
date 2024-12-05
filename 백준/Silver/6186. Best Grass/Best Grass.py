#3W_2일차_1번문제 : connected components
'''
[문제분석]
- 목초 구역의 개수 구하기(?)
- 입력
    1. 행의 수 R 열의 수 C (공백 구분)
    2. R만큼 반복, C만큼 풀이 심어져 있는 곳 표시
        - 풀이 심어져 있는 구역은 '#', 없으면 '.'
- 출력 : 목초지의 개수

[문제해결과정]
인접한 노드끼리 묶어서 연결된 컴포넌트의 개수를 구하면 됨.
- count = 0
- 입력값 받는 for문 -> 이차원 배열 저장할 리스트 land = []
- 매트리스는 이중 for문 -> 모든 노드 방문
- 모든 노드를 방문해서 인접노드가 없으면 count += 1
- 방법
    1. dfs로 풀기(우선)
        - stack = []
        - hash set 필요 seen = set() : 한 번 방문한 노드 기록용
        - 문제는, 인접노드를 어떻게 확인하냐는 것.
        '#'의 위치를 파악하고 좌표값을 stack, seen에 추가
        stack에서 pop을 해서 directions값과 연산해서
        일치하는 값이 있으면 count += 1해주면 될듯?
        ->stack이 빌때까지(while stack:)
    


    2. bfs로 풀기

'''
#코드

land = []
stack = []
seen = set()
count = 0
#인접노드
direction = [(-1,0), (1,0), (0,-1),(0,1)]

#입력값 받는 부분
R, C = map(int, input().split())

for _ in range(R):
    grass = input() #잔디 여부를 입력받고
    land.append(grass)

#탐색
for i in range(R):
    for j in range(C):
        #방문한 노드가 '#'이면 stack, seen에 좌표 추가
        if land[i][j] == '#':
            stack.append((i, j))
            count+= 1

while stack:
    x, y = stack.pop()

    for dx, dy in direction:
        if (x+dx, y+dy) in stack:
            seen.add((x, y))
            count -= 1


print(count)

