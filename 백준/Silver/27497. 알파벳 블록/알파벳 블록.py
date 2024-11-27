#2W_1일차_1번문제 : 문자열 조합
"""
[요구사항]
- 알파벳 블록을 일렬로 조립하여 문자열 생성
- 각 블록에는 문자하나
- 세 개의 버튼
    1. 문자열 맨 뒤 블록 추가
    2. 문자열 맨 앞 블록 추가
    3. 문자열에서 가장 나중에 추가된 블록 제거
- 빈 문자열로 시작, 빈 문자열일 때 3번 버튼 -> 동작 X
- 버튼 누른 횟수(N)와 누른 버튼(1/2/3)이 순서대로 주어질 때 완성된 문자열 구하기

- 입력 형식
    1. 입력 첫째 줄 : 버튼 누른 횟수 N
    2. 입력 둘쨰 줄 ~ : 버튼종류 해당문자
        ex. 1 c : 문자열 맨 뒤에 c가 적힌 블록 추가
-  출력 형식
    완성된 문자열 출력, 빈 문자열인 경우 0 출력

[문제분석_의사해결과정]
- 입력값 처리 : N을 입력받고, N번 반복하면서 각 명령어(cmd) 처리
(for문)
- 명령어 처리
    1. LIFO 스택구조네? 
        if문)
        - 버튼 1: append
        - 버튼 2: insert(0, 값)
        - 버튼 3: pop()
        - (isEmpty() ? "0")
    2. 스택 처리 배열 stack = []
    3. 빈 문자열 처리 포함 print
    """
    #코드1 : Fail >> 버튼 3의미를 잘 못 파악.stack에서 가장 끝에 있는 블록을 빼는 게 아니라 시간적으로 나중에 들어온 블록을 빼야함.
'''
stack = []

N = int(input())

for _ in range(N):
    cmd = input().split()

    if int(cmd[0]) == 1:
        stack.append(cmd[1])
        
    elif int(cmd[0]) == 2:
        stack.insert(0, cmd[1])
        
    elif int(cmd[0]) == 3:
        if stack:
            stack.pop()
    print(stack)
        
print(0 if not stack else stack)            
'''
#코드2 : 순서관리 배열 order 추가 => Fail >> 시간초과

# deque()로 변경
import sys
from collections import deque

stack = deque()
order = deque()

N = int(sys.stdin.readline())

for _ in range(N):
    cmd = sys.stdin.readline().split()

    if int(cmd[0]) == 1:
        stack.append(cmd[1])
        order.append("back")
        
    elif int(cmd[0]) == 2:
        stack.insert(0, cmd[1])
        order.append("front")
        
    elif int(cmd[0]) == 3:
        if stack:
            latest = order.pop()
            if latest == "back":
                stack.pop()
            else:
                stack.popleft()
    # print(stack)

print(0 if not stack else "".join(stack))