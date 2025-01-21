#문제 1010번 : 다리놓기
'''
[상황]
강의 서쪽 : N개
강의 동쪽 : M개
1. N <= M개
2. N개의 다리를 지으려고 함
3. 한 사이트에는 최대 한 개의 다리만 연결
3. 다리끼리는 서로 겹쳐질 수 없음
4. 다리를 지을 수 있는 경우의 수를 구하여라.

[입력]
1. 첫번째 줄 : 테스트 케이스 개수 T
2. 이후 T개의 줄 : N, M (공백기준)

[출력]
각 테스트 케이스에 대해 다리를 지을 수 있는 경우의 수

[문제 해결 과정]
0-1. 조합 : 서로 다른 n개중에 r개를 선택하는 경우의 수
0-2. dp : 조합 C(m, n) => dp[m][n]
     - 행이 m, 열이 n => m개의 항목 중에서 n개를 선택하는 경우의 수
     - ex. dp[m][0] = 1 : 어떤 m에서든 0개를 선택하는 경우는 1가지.
        dp[m][m] = 1 : 어떤 m에서든 m개를 선택하는 경우는 1가지
     - 재귀 관계 적용 : 
     C(m, n) = C(m-1, n-1) + C(m-1, n)
     dp[m][n] = dp[m-1][n-1] + dp[m-1][n]
1. bottom up 방식: 아래에서부터 계산을 수행하고 그 값을 누적시켜서 전체 큰 문제를 해결해나가는 방식
   cf. top down 방식으로도 풀 수 있으나 bottom up방식에 비해 재귀호출의 오버헤드가 우려됨으로 X

2. dp 2차원 배열 생성
3. n이 1인 경우 = 출력값도 1
'''
import sys
input = sys.stdin.readline

def bridge(n, m):
    # DP 테이블 초기화
    # 기준이 서쪽이니까 n행 m열로 만들어주기
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    
    for i in range(1, n+1): #행
        for j in range(1, m+1): #열
            if i == 1:
                dp[i][j] = j 
            elif i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

    return dp[n][m]
    

#입력값처리부분
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(bridge(n, m))