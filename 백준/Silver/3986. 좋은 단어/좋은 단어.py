#2w_1일차_3번문제
'''
[요구사항]
- 입력
첫째 줄 입력값: 단어 수 N
둘째 줄 ~ : A, B로만 이루어진 단어가 한 줄에 하나씩
- 좋은 단어 조건:
    1. 단어 위로 아치형 곡선으로 그려 같은 글자(AA, BB)끼리 쌍을 지었을 때
    2. 선끼리 교차하지 않으면서 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝을 지을 수 있어야
- 출력 : 좋은 단어의 수

[문제 해결 과정]
1. 쌍을 이룬다.
2. 대부분 쌍을 이루어 판단하는 문제들은 stack을 활용한 문제라는 생각.
    - 쌍을 이루면 좋다 => a를 찾고, 그 다음도 a면 상쇄한다
    - 쌍을 이루지 못한다 => a가 있고, 그 다음 b이면 a에 b가 추가된다.
    - 결국 result 배열에 요소들끼리 상쇄가 되어 비어있다면 good
    - 요소가 남아있으면 false
그렇다면,
3. N으로 입력받을 단어의 수 정하고 for문 생성 for _ in range(N)
4. 좋은 단어임을 판별하는 데 쓰일 빈 스택 생성
    result = []
5. 문자열 word 입력 받기 word = sys.stdin.readline()
6. for문으로 word의 요소를 돌면서 for char in word:
7. result가 비어있다면 char을 push해주고
8. 그렇지 않다면 result[-1]과 비교해서 같으면 pop()
9. result[-1]과 달라도 char을 push
10. stack이 비어있다면 count +1
11. 개수를 출력하는 게 목적이므로 count 변수 필요
12. count 출력
'''
#코드
import sys

N = int(sys.stdin.readline())
count = 0

for _ in range(N):

    word = sys.stdin.readline().strip()
    result = []

    for char in word:
        if result and result[-1] == char:
            result.pop()
        else:
            result.append(char)
    
    if not result:
        count += 1

print(count)
    
