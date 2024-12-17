import sys

input = sys.stdin.readline
N = int(input())
result = 1
count = 1

if N == 0:
    count = 0

else:
    while result < N:
        result *= 2  # 두 배로 증가
        count += 1

print(count)
