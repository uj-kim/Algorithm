#2W_2일차_4번문제 : Queue
'''
[요구사항]
- 정수를 저장하는 큐를 구현하고, 입력으로 주어지는 명령 처리
- 명령의 종류
    1. push X: 정수 X를 큐에 추가
    2. pop : 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력(정수가 없는 경우 -1 출력)
    3. size : 큐에 들어있는 정수의 개수
    4. empty : 큐가 비어있으면 1, 아니면 0 출력
    5. front : 큐의 가장 앞에 있는 정수 출력(없는 경우 -1)
    6. back : 큐의 가장 뒤에 있는 정수 출력(없는 경우 -1)

- 입력
    1. 첫째 줄 : 명령 수 N
    2. 둘째 줄 ~ : 명령

- 출력 : 명령실행결과 출력

[문제 해결 과정]
1. 첫번째로 받을 입력 : 명령의 수 N -> int(input())
2. 간단하게 deque로 해결해야겠다 
-> from collections import deque
   queue = deque()
3. N개의 명령 수행 -> for _ in range(N):
4. 명령 입력 받기 cmd = input().split()
5. for문 안에서 if문으로 명령 종류 판별
    - 1. push X : queue.append(X) -> X값 인덱스로 추출
    - 2. pop : print(queue.popleft())
    - 3. size : print(len(queue))
    - 4. empty :1 if not queue else 0
    - 5. front : print(queue[0])
    - 6. back : print(queue[-1])
    - pop, front, back => 명령수행 if not stack else -1
'''
#코드
import sys
from collections import deque

N = int(input())
queue = deque()

for _ in range(N):

    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        X = int(cmd[1])
        queue.append(X)

    elif cmd[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())

    elif cmd[0] == "size":
        print(len(queue))

    elif cmd[0] == "empty":
        print(1 if not queue else 0)
    
    elif cmd[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif cmd[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])