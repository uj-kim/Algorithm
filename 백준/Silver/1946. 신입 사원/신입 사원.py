#3W_1일차_2번문제
'''
[문제분석]
- 1차 서류심사, 2차 면접시험
- 다른 지원자보다 1차, 2차 모두 성적이 낮으면 FAIL
- 최대 채용인원수
- 입력
    1. 첫째줄 : 테스트 케이스 개수 T
    2. 테스트 케이스의 첫째줄 : 지원자 숫자 N
    3. 테스트 케이스 2~N째줄 : 서류, 면접 성적 순위(공백 구분, 동석차 없음)
- 출력 : 테스트케이스 별 선발할 수 있는 신입사원 최대 인원 수 

[문제 해결 과정]
1. 입력값 
    - 테스트 케이스 개수 T
    - for문T :테이스케이스별 지원자 수 N
    - for문N : 서류순위, 면접순위 (공백구분)
        변수명 : p_rank, i_rank
    
2. 서류를 기준으로 오름차순 정렬
3. 서류 1등한 사람을 기준으로 이 사람보다 면접 성적이 높다면?
    => 선발 기준을 만족시킴.

4. 방법 생각
    4-1. input 받은 값을 리스트에 넣어서 sorted하고 for문 돌리기 => O(n log n)
    4-2. heappush로 바로바로 정렬해주기 => O(n log n)
    4-3. min으로 서류 1등을 찾아서. 서류 1등의 면접 성적을 기준으로 잡고 갱신하면서 for문 돌리기 => 시간복잡도는 O(n)예상
=> 1번이 제일 직관적이고 구현하기 간단할 것 같다.(정렬 후 순회)
   2번 같은 경우에는 최소값을 구하고, 어차피 또 for문 돌려야 하므로. 최소값을 구하는 방식도 굳이 heap을 쓸 이유가 없다.
   3번은 시간복잡도는 제일 낮아도 코드가 불필요하게 길어질듯.
   (추후 시도)
'''
#코드
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N = int(input())
    participants = sorted([tuple(map(int,input().split())) for _ in range(N)])
    
    count = 1
    min_standard = participants[0][1]

    for i in range(1, len(participants)):
        if participants[i][1] < min_standard:
            count += 1
            min_standard = participants[i][1]

    print(count)