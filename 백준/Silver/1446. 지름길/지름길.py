#문제 : 세준이가 운전해야하는 거리의 최솟값 출력
'''
[입력]
1. 첫째 줄 : 지름길 개수 N, 고속도로 길이 D(공백 구분)
2. ~ N개 줄 : 지름길 시작 위치, 도착위치, 지름길 길이(공백구분)

[출력]
세준이가 운전해야하는 거리의 최솟값출력

[문제해결과정]
1. 문제 이해 => A|-----------------------|B 고속도로 길이
2. 중간중간 지름길이 있어서 A에서 B까지 원래의 길이가 150이라고 하면
3. 100만 운전해도 B에 도착할 수 있음. 
4. dp, 다익스트라로 푸는 문제 같음.
[dp]
0. dp테이블을 만들어주고
1. dp[i]를 고속도로의 위치i에 도착할 때까지 운전한 최소거리라고 정의
2. 목표는 dp[D]를 구하는 것.
3. dp[0] = 0(고속도로 시작점)


'''
import sys

input = sys.stdin.readline

N, D = map(int, input().split())

dp = [i for i in range(D+1)]

shortcuts = []

for _ in range(N):
    start, end, length = map(int, input().split())
    if end <= D:
        shortcuts.append((start, end, length))

shortcuts.sort()

for start, end, length in shortcuts:
    for i in range(1, D+1):
        if end == i:
            dp[i] = min(dp[i], dp[start]+length)
        else:
            dp[i] = min(dp[i], dp[i-1]+1)   
        
print(dp[D])