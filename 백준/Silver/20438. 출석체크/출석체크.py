# 문제 : 출석체크

import sys

input = sys.stdin.readline

# Step 1: 입력 받기
n, k, q, m = map(int, input().split())

# Step 2: 졸고 있는 학생 표시
sleep_students = list(map(int, input().split()))
sleep = set(sleep_students)  # 빠른 조회를 위해 set 사용

# Step 3: 출석 상태 초기화 (False: 출석하지 않음, True: 출석함)
all_students = [False] * (n + 3)  # 인덱스 0,1,2는 사용하지 않음

# Step 4: 출석 코드 발송 처리
calling = list(map(int, input().split()))
for sender in calling:
    if sender < 3 or sender > n + 2:
        continue  # 유효하지 않은 번호는 무시
    if sender in sleep:
        continue  # 졸고 있는 학생은 무시
    for j in range(sender, n + 3, sender):
        if j in sleep:
            continue  # 졸고 있는 학생은 무시
        all_students[j] = True  # 출석 표시

# Step 5: 누적합 배열 생성 (출석하지 않은 학생 수)
prefix_not_attended = [0] * (n + 3)
for i in range(3, n + 3):
    prefix_not_attended[i] = prefix_not_attended[i - 1] + (0 if all_students[i] else 1)

# Step 6: 구간 쿼리 처리 및 출력
for _ in range(m):
    s, e = map(int, input().split())
    # 입장 번호는 3부터 N+2까지이므로 범위를 조정
    s = max(s, 3)
    e = min(e, n + 2)
    if s > e:
        not_attended = 0
    else:
        not_attended = prefix_not_attended[e] - prefix_not_attended[s - 1]
    print(not_attended)
