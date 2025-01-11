'''
문제: 돌려막기
[상황]
급하게 처리해야 할 일이 생김.
각자 최종 일량을 계산해 가장 안 바쁜 사람이 일을 처리하기로 정함.
인원 : 인서, 준석, 정우, 진우, 영기 (5명)
일의 개수 : 5
- 행렬 A : 일의 예상 난이도를 각 행에 나열.
- 행렬 B : 일의 예상 처리시간을 각 행에 나열
- 개인 최종 일량 = (일의 난이도 x 일의 처리시간) 총 합(1~5개)
- 최종 일량이 가장 적은 사람이 가장 일이 안 바쁜 사람

[입력]
행렬 A (5x5) 1~ 5줄
행렬 B (5x5) 6 ~ 10줄

[출력]
영문 이름 출력
'''
# import sys
# input = sys.stdin.readline

names = ["Inseo","Junsuk", "Jungwoo","Jinwoo","Youngki"]
A = []
B = []

for _ in range(5):
    A.append(list(map(int, input().split())))

for _ in range(5):
    B.append(list(map(int, input().split())))

# 각 인원의 총 일량 계산
total_workloads = [0] * 5 

for x in range(5):  
    for y in range(5):
        workload = 0
        for i in range(5):
            workload += A[x][i] * B[i][y]
        total_workloads[x] += workload

min_workload = min(total_workloads)
# min_index = total_workloads.index(min_workload)

for i in range(len(total_workloads)):
    if total_workloads[i] == min_workload:
        min_index = i


print(names[min_index])