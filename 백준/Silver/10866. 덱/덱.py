#2W_1일차_2번문제 : Deque 덱
'''
[요구사항]
정수를 저장하는 덱(Deque)을 구현, 입력으로 주어지는 명령 처리 프로그램 작성
- 명령
    1. push_front X: 정수 X를 덱의 앞에 넣기
    2. push_back X: 정수 X를 덱의 뒤에 넣기
    3. pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력(없는 경우 -1)
    4. pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력(없는 경우 -1)
    5. size: 덱에 들어있는 정수 개수 출력
    6. empty: 덱이 비어있으면 1, 아니면 0 출력
    7. front: 덱의 가장 앞에 있는 정수 출력(없는 경우 -1)
    8. back: 덱의 가장 뒤에 있는 정수 출력(없는 경우 -1)
- 입력 
    1. 첫째 줄 : 명령 수 N
    2. 둘째 줄 ~ : 8가지 명령 중 택 1

- 출력 : 명령마다 한 줄에 하나씩


[문제 해결 과정]
1. 받을 명령의 수 N 입력값 받기
2. for 문 안에 if-elif-else, print
3. 명령어
    1. push_front X : appendleft(X)
    2. push_back X : append(X)
    3. pop_front: popleft()
    4. pop_back: pop()
    5. size: len(result)
    6. empty: 1 if not result or 0
    7. front: result[0]
    8. back: result[-1]
3-1. 3, 4, 7, 8 => 덱에 정수가 없는 경우 : else로 -1
4. result = deque()
'''
#코드
import sys
from collections import deque

N = int(sys.stdin.readline())
result = deque()

for _ in range(N):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == "push_front":
        X = int(cmd[1])
        result.appendleft(X)
    elif cmd[0] == "push_back":
        X = int(cmd[1])
        result.append(X)
    elif cmd[0] == "pop_front":
        print(-1 if not result else result.popleft())
    elif cmd[0] == "pop_back":
        print(-1 if not result else result.pop())
    elif cmd[0] == "size":
        print(len(result))
    elif cmd[0] == "empty":
        print(1 if not result else 0)
    elif cmd[0] == "front":
        print(-1 if not result else result[0])
    elif cmd[0] == "back":
        print(-1 if not result else result[-1])
