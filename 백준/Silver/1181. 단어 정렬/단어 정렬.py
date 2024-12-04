#3W_1일차_4번문제
'''
[문제 분석]
- 알파벳 소문자로 이루어진 N개의 단어를 조건에 따라 정렬
    1. 길이가 짧은 순
    2. 길이가 같다면 사전 순
    3. 중복 단어는 중복 제거
- 입력
    1. 첫째 줄 : 단어 개수 N
    2. 2 ~ N줄 : 알파벳 소문자로 이루어진 단어 한 줄에 하나씩
- 출력 : 조건에 따라 정렬된 단어 출력

[문제 해결 과정]
0. 가장 먼저 떠오른 메서드
    => 중복제거 set()
    => 정렬 sorted
1. 길이 우선 -> len()을 기준으로
2. 동일한 길이라면?
3. sorted()의 여부
4. 입력값 
    - 단어의 개수 N
    - N개의 단어 -> 빈배열 words를 생성해주고 넣어주자
        => set으로 바로 만들 수 있을까? 안 됨. list -> set 변환
5. 출력은 N줄에 걸쳐서

'''
#코드
import sys
import heapq

N = int(sys.stdin.readline())
words = []

for _ in range(N):
    word = sys.stdin.readline().split()
     #단어가 리스트로 들어가기 떄문에 그냥 문자열로 한 리스트 안에 추가해줌 -> extend
    words.extend(word)
#길이순, 사전순 => lambda로 한꺼번에f

#set으로 중복제거를 나중에 해주면, set의 특성상 순서를 뒤바꿔버리기 때문에 안 됨
# result = set(sorted(words, key = lambda x: (len(x), x)))

result = sorted(set(words), key = lambda x: (len(x), x))
for i in result:
    print(i)
