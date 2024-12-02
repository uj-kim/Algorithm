#2W_5일차_3번 문제
'''
[문제 분석]
- 리스트에 있는 번호들을 가진 티켓을 제외한 티켓 중 번호가 가장 작은 티켓의 번호 찾기

- 입력 
    1. 첫째 줄: 1차 티켓팅에서 팔린 티켓들의 수 N
    2. 둘째 줄 1차 티켓팅에서 팔린 티켓들의 번호 A
- 출력 : 2차 티켓팅에서 가질 수 있는 티켓 중 가장 작은 번호

[문제해결과정]
1. 정수 N 입력값 받기
2. N만큼의 티켓번호 한 줄에 공백 구분지어 받기

'''
#코드
import sys

N = int(sys.stdin.readline())

sold_tickets = sorted(list(map(int,sys.stdin.readline().split())))

ticket_num = 1

for i in sold_tickets:
    if ticket_num == i:
        ticket_num += 1
    else:
        break;

print(ticket_num)

