N, M = map(int, input().split())

# 알고 있는 노래 저장
know_songs = []
for _ in range(N):
    data = input().split()
    title = data[1]  # 노래 제목
    first_three_notes = data[2:5]  # 첫 세 음
    know_songs.append((title, first_three_notes))

# 시도하는 음 저장
challenges = []
for _ in range(M):
    challenge = input().split()
    challenges.append(challenge)

# 결과 처리
results = []
for challenge in challenges:
    matching_titles = []
    for title, notes in know_songs:
        if notes == challenge:  # 첫 세 음이 동일한 경우
            matching_titles.append(title)
    
    if len(matching_titles) == 1:
        results.append(matching_titles[0])  # 하나만 일치
    elif len(matching_titles) > 1:
        results.append("?")  # 여러 개 일치
    else:
        results.append("!")  # 없음

# 출력
for result in results:
    print(result)
