#3W_2일차_4번문제 : 그래프 정점과 간선의 이해
'''
[문제 분석]
- 가장 적은 종류의 비행기를 타고 모든 국가를 여행할 수 있도록
- 입력
    1. 테스트 케이스 수 T
        - 국가의 수 N, 비행기 종류 M(공백 구분)
        - ~ M개의 줄 : a국가 b국가 
- 출력 : 테스트케이스별 비행기 종류의 최소 개수
'''
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
    print(N-1)