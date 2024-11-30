#2W_4일차_4번 문제
'''
[요구사항]
- 입력 : 
    1. 첫째 줄 : 테스트 케이스의 개수
    2. 테스트 케이스의 첫째 줄 : 해빈이가 가진 의상 수
    3. 테스트 케이스의 n개 줄 : 해빈이가 가진 의상 이름, 종류 (공백으로 구분)
        - 같은 종류의 의상은 하나만 입을 수 있음
- 출력
    : 각 테스트 케이스에 대해 해빈이가 알몸이 아닌 상태로 의상을 입을 수 있는 경우

[문제 해결 과정]
1. 입력 첫 번째 줄 : 테스트 케이스의 개수 case => int(input())
2. 테스트 케이스 별로 의상 이름, 종류를 받아야 하므로
 => 중첩 for문? 더 좋은 방법이 있을까 모르겠다
3. for _ in range(case):
    3-1. 의상 수 input받기 => n = int(input())
    3-2. 의상 수에 따라 의상이름, 종류 input 받기
        => 딕셔너리를 활용할건데,,
        => 딕셔너리의 형태는 {종류 : 개수}
        => closet = {}
    3-3. for _ in range(n):
        clothes = sys.stdin.readline().split()
        만약 같은 종류가 이미 있다면 (if문):
            closet[clothes[1]] += 1 값(개수) 증가
        없으면 딕셔너리 생성(값은 1)

4. 이 이후에는 '조합'을 이용해서 경우의 수를 구해야 할텐데
    => 각 종류의 개수 + 1 (1은 착용 안 했을 경우를 추가해준 것)를 모두 곱해준다음 - 1(아무것도 안 입은 경우를 제외) 해주기
    - 초기값 설정 : pairs = 1
    for val in closet.values():
        pairs *= (val + 1)
    
5. 경우의 수 출력 => print(pairs - 1)
'''
#코드
import sys

case = int(input())

for _ in range(case):
    n = int(input())
    closet = {}

    for _ in range(n):
        clothes = sys.stdin.readline().split()
        
        if clothes[1] in closet:
            closet[clothes[1]] += 1
        else:
            closet[clothes[1]] = 1

    pairs = 1
    for val in closet.values():
        pairs *= (val + 1)

    print(pairs - 1)





        