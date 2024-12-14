#정보상인호석
#문제 해결 방법:
'''
[문제]
- 입력
    1. 첫째 줄 : 쿼리의 개수 Q
    2. ~Q개의 줄(쿼리)
        - 1로 시작 => 정보 판매자 정보
          : 1 정보제공자이름 정보개수k 정보의가치(k개)
        - 2로 시작 => 호석이의 정보거래내역
          : 2 구매자이름 정보개수b

- 과정
    - 호석이는 정보제공자가 가진 정보들 중 가장 비싼 b개를 구매.
    - 고릴라가 가진 정보가 b개 이하면 모든 정보를 구매
    - 호석이가 구매한 정보들의 가치(=쓴 돈)의 총합

- 출력
    : 모든 쿼리가 종료되었을 때에 호석이가 얻게되는 정보 가치의 총합

[문제해결과정]
0. 어떻게 풀 것인가?
    - 나열된 요소 중 최대 값을 뽑아서 파기한다 => "heapq"
1. 입력받을 줄의 양 Q
2. 줄 별로 요소 판단 => for _ in range Q해서
    - 입력값은 공백 구분해서 cmd 변수로 받기
    - 인덱스로 판단
    - 딕셔너리 X heapq 조합
        1. 사전에 gorillas = dict() 생성
        2. 인덱스 활용 부분
            - cmd[0] == 1 or 2
            - if 1이라면 : 
                고릴라이름, 가지고 있는 정보 개수(k), k개의 정보들(list)을
                각각 변수에 담아주고
                list 요소를 돌면서 gorilla[고릴라이름]에 heappush
                (최댓값이니까 음수로)
            - if 2라면:
                gorilla[고릴라명] 확인 -> 결과에 heapop한 값 더해주기
3.결과 출력

- 필요 변수
    1. Q : int, 입력값처리에 활용
    2. cmd : 입력값처리에 활용, 공백구분(split)
    3. gorillas : dict, 해당이름의 고릴라가 가지고 있는 정보
    4. name : str, 고릴라 이름
    5. k : int, 해당 고릴라가 가지고 있는 정보의 개수
    6, infos : list, 해당 고릴라가 가지고 있는 k개의 정보의 가치
    4, result : int, 뽑아낸 최댓값을 합산해주는 용도(0으로 초기화)
- 활용 메서드 
    1. heapq => heappush, heappop
'''
#코드
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

gorillas = defaultdict(list)
result = 0

Q = int(input())

for _ in range(Q):
    cmd = input().split()


    if cmd[0] == '1':
        name = cmd[1]
        infos = list(map(int,cmd[3:]))

        for val in infos:
            heapq.heappush(gorillas[name], -val)


    elif cmd[0] == '2':
        name = cmd[1]
        if gorillas[name]:
            b = int(cmd[2])
            if b >= len(gorillas[name]):
                result += sum(gorillas[name])
                gorillas[name].clear()
            else:
                for _ in range(b):
                    result += heapq.heappop(gorillas[name])
    else:
        break;

print(-result)