#2W_2일차_1번문제:
'''
[요구사항]
N개의 막대기에 대한 높이 정보가 주어질 때, 오른쪽에서 보아서 몇 개가 보이는 지
1. 첫 번째 입력줄 : 막대기의 개수 정수 N
2. 두 번째 입력줄 ~ : 막대기의 높이 정수 h
3. 오른쪽에서 N개의 막대기를 보았을 때, 막대기의 개수 출력

[문제 해결 과정]
1. 입력값받은 배열 stack
2. 결과 담을 배열 result
3. stack에서 최대값인 요소의 인덱스 추출 
4. 오른쪽에서 보이는 시선이므로 stack을 reverse해서 탐색

'''
#코드
import sys

N = int(sys.stdin.readline())

stack = []
result = []

for _ in range(N):
    h = int(sys.stdin.readline())
    stack.append(h)

max_index = stack.index(max(stack))
stack = stack[max_index:]

for x in reversed(stack):
    if not result or x > result[-1]:
        result.append(x)

print(len(result))