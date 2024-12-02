#2W_5일차_1번 문제 : 팀명 정하기
'''
[문제 분석]
- 팀 이름 짓는 법
    1. 세 참가자의 입학년도를 100으로 나눈 나머지를 오름차순 정렬해서 이어 붙인 문자열
    2. 세 참가자 중 성씨를 영문으로 표기했을 때의 첫 글자를 백준 온라인 저지에서 해결한 문제가 많은 사람부터 차례대로 나열한 문자열
- 세 팀원이 해결한 문제 개수, 입학년도, 성씨가 주어짐
- 방법 1, 2대로 만들어진 팀명을 차례로 출력
- 입력
    0. 팀원 정보 형식 : 문제 개수 P, 입학년도 Y, 성씨 S (공백구분)
    1. 첫째 줄 : 첫 번째 팀원의 정보
    2. 둘째 줄 : 두 번째 팀원의 정보
    3. 셋째 줄 : 세 번째 팀원의 정보

- 출력
    1. 첫째 줄 : 첫 번째 방법으로 만든 팀명
    2. 둘째 줄 : 두 번째 방법으로 만든 팀명

[문제 해결 과정]
1. 3명의 팀원 정보 : for 문 in range(3)
2. sorted()를 써서 1번 기준으로 해서 way1
3. sorted()를 써서 p를 기준으로 내림차순 -> way2

'''
#코드
import sys

team = []
result1 = ""
result2 = ""
for _ in range(3):
    p, y, s = sys.stdin.readline().split()
    team.append((int(p), y[2:], s))

    way1 = sorted(team, key=lambda x: x[1])
    way2 = sorted(team, key=lambda x: x[0], reverse = True)
for i in way1:
    result1 += i[1]

for i in way2:
    result2 += i[2][0]
print(result1)
print(result2)
# print(team)