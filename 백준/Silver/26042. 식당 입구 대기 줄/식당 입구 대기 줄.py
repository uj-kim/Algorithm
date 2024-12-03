import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
students= deque()
max_wait = 0
last_std = None

for _ in range(n):
    info = input().split()
    if len(info) == 1:
        if students:
            students.popleft()
    else:
        student = int(info[1])
        students.append(student)
        if len(students) > max_wait:
            max_wait = len(students)
            last_std = student
        elif len(students) == max_wait:
            last_std = min(last_std, student)

print(max_wait, last_std)
