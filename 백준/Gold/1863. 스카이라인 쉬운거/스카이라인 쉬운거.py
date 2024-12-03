import sys
input = sys.stdin.readline

n = int(input())
stack = []
count = 0

for _ in range(n):
    x, y = map(int, input().split())

    # 스택의 top이 현재 높이보다 높으면 pop하고 count 증가
    while stack and stack[-1] > y:
        stack.pop()
        count += 1

    # 스택이 비어있거나 스택의 top이 현재 높이보다 낮으면 현재 높이 push
    if not stack or stack[-1] < y:
        stack.append(y)

# 스택에 남아있는 높이들 처리
while stack:
    if stack.pop() > 0:
        count += 1

print(count)
