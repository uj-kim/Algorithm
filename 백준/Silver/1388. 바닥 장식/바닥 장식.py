#3W_2일차_2번문제 :
'''
[문제 분석]
- 바닥에 몇 개의 나무판자가 필요한가
- '-'와 '|'로 이루어진 바닥 장식 모양
- 두 개의 '-' 혹은 두 개의 '|'가 인접해 있으면 같은 나무 판자로 취급
- 입력
    1. 방 바닥 정보 : 세로크기 N, 가로크기 M (공백 구분)
    2. ~ N 개의 줄 : M개의 문자('-' 혹은 '|')

- 출력 : 문제의 정답(방바닥을 장식하는데 필요한 나무 판자의 개수)

[문제 해결 과정] "입력 -> 탐색 -> 출력"
1. 인접한 문자를 기준으로 나무판자의 개수를 구하는 문제 => connected components
2. dfs / bfs => bfs로 풀어볼까?
3. 입력값 처리
    - N, M = map(int, input().split())
5. floor = []
. 판자 개수를 나타내는 count 변수 count = 0
4. N개의 줄에 M개의 문자 받기
    => for문(N)
        - wood = input()
        -> floor에 wood를 append()로 추가
5. 모든 노드를 방문.(이중 for문)
6. visited 


5. 인접노드 탐색.
    - 행을 기준 '-'이 연속 -> 같은 판자 
    - 열을 기준 '|'이 연속 -> 같은 판자

'''
#코드
from collections import deque

#입력
N, M = map(int, input().split())

floor = []
count = 0
visited = [[False for _ in range(M)] for _ in range(N)]

for _ in range(N):
    floor.append(input())
    
    #1차원 배열이지만 문자열요소이기 때문에 괜찮음

#탐색
#모든 노드 방문
for i in range(N):
    for j in range(M):
        #방문한 적이 없는 인자   
        if not visited[i][j]:
            count += 1

            #인접노드 탐색(bfs) -> 동일하다면 방문 취급
            queue = deque()
            queue.append((i,j))
            visited[i][j] = True

            #queue가 빌 때까지 반복
            while queue:
                x, y = queue.popleft()
                
                #분기('-'인접)
                if floor[x][y] == '-':
                    if y+1 < M and not visited[x][y+1] and floor[x][y+1] == '-':
                        queue.append((x, y+1))
                        visited[x][y+1] = True
                #분기('|'인접)
                elif floor[x][y] == '|':
                    if x + 1 < N and not visited[x+1][y] and floor[x+1][y] == '|':
                        queue.append((x+1, y))
                        visited[x+1][y] = True

print(count)



    