"""

- 문제
  같은 울타리 영역 안의 양들의 숫자가 늑대의 숫자보다 더 많을 경우 늑대가 전부 잡아먹힌다.
  물론 그 외의 경우는 양이 전부 잡아먹히겠지만 말이다.

  꿍은 워낙 똑똑했기 때문에 이들의 결과는 이미 알고있다.
  만약 빈 공간을 '.'(점)으로 나타내고 울타리를 '#', 늑대를 'v', 양을 'k'라고 나타낸다면
  여러분은 몇 마리의 양과 늑대가 살아남을지 계산할 수 있겠는가?
- 입력
  입력의 첫 번째 줄에는 각각 영역의 세로와 가로의 길이를 나타내는 두 개의 정수 R, C (3 ≤ R, C ≤ 250)가 주어진다.
  다음 각 R줄에는 C개의 문자가 주어지며 이들은 위에서 설명한 기호들이다.
- 출력
  살아남게 되는 양과 늑대의 수를 각각 순서대로 출력한다.
- 예제 입력

- 예제 출력

- 문제 분석
  늑대 >= 양 -> 양 다죽음 
  늑대 < 양 -> 늑대 다죽음
  
  . : 빈공간
  # : 울타리 
  v : 늑대 
  k : 양 

  
  ** SUDO CODE **
  입력 
   1. r,c int로 입력받음 (가로 세로)
   2. for _ in range(r)
   3. 입력받은 c를 저장할 [] 초기화 
   4. 출력을 위한 양, 늑대 카운트 변수로 초기화

  구현 
  1. 탐색은 BFS를 사용해서 탐색 
  2. queue를 사용
  3. 방문한 노드를 기록하기 위한 행렬 visited 생성 <내부 값은 true, false로 설정
  4. 인접 노드를 탐색함 상,하,좌,우를 설정해준다. dx = [1,-1,0,0], dy = [0,0,-1,1] 

  5. for i in range(r):
  6. for j in range(c):
  7. if #이 아니고 false인 곳 만 탐색 시작  
  8. 여기서 q가 들어간다.
  9. 탐색이 시작되면 해당 노드는 true로 변경해준다.

  10. 양, 늑대 변수 설정 
  11. 해당 좌표에 k가 있으면 k + 1, v가 있으면 v + 1 
  13. while q 
  12. 인접노드를 dx dy를 사용해서 탐색한다. 
  14. q.pop으로 좌표를 뽑아서 변수에 할당
  15. dx, dy를 설정해서 새로운 nx, ny를 만들어준다. 
  16. land(c x r) 의 크기를 벗어나지 않는 . < indexError 방지 
  17. if 상하좌우도 false인
  18. if #이 아닌 곳만 탐색
  19. q.append( nx , ny )
  20. 방문을 햇으니 lan(nx, ny)  = true
  21. if k ==> k + 1
  22/ if v --> v + 1
  23. while 바깥에서 늑대와 양의 수를 비교 K > v 
    늑대 >= 양 -> 양 다죽음 
    늑대 < 양 -> 늑대 다죽음
  24. 초기에 설정했던 전역변수로 선언했던거에 += k, v 
  25. 전역변수 양 늑 print 
  ------
  ..#..
  #..#.
  #..#.+
  #.#..
  ------
  7. 
  출력 
  1. 양, 늑대 출력
- 코드 구현
  """

import sys
input = sys.stdin.readline
from collections import deque

def bfs(start_x,start_y):
  global total_sheep, total_wolf
  
  q = deque([(start_x,start_y)])
  visited[start_x][start_y] = True
  sheep, wolf = 0, 0
  if land[start_x][start_y] =="v":
    wolf += 1
  elif land[start_x][start_y] == "k":
    sheep += 1

  while q: 
    x, y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 인덱스 에러 방지  - 가 되면 안되고 r,c를 초과해도 안댐 
      if 0 <= nx < r and 0 <= ny < c: 
        if visited[nx][ny] == False and land[nx][ny] != "#":
          visited[nx][ny] = True
          if land[nx][ny] == 'k':
            sheep += 1
          elif land[nx][ny] == 'v':
            wolf += 1
          q.append((nx,ny))
  if wolf < sheep: 
    total_sheep += sheep 
  else :
    total_wolf += wolf 

r,c = map(int, input().split())

land = []
for _ in range(r):
  land.append(input())

total_sheep = 0
total_wolf = 0

dx = [1,-1,0,0]
dy = [0,0,-1,1] 

visited = [[False]*c for _ in range(r)]

for i in range(r):
  for j in range(c):
    if land[i][j] != "#" and visited[i][j] == False:
      bfs(i,j)
  
print(total_sheep, total_wolf)

