#2번문제
'''
[문제]
- N개의 수를 대표하는 기본 통계값
1. 산술평균 : sum(N) / N
2. 중앙값 : mid(N)
3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
4. 범위 : max(N)-min(N)

- N개의 수가 주어졌을 때 네가지 기본 통계값을 구하는 프로그램

- 입력
    1. 첫째 줄 : N (isOdd)
    2. N개 줄 : 정수(<=4000)
- 출력
    1. 산술평균(소수점이하 첫째자리에서 반올림)
    2. 중앙값
    3. 최빈값(여러개일 경우 두 번째로 작은 최빈값)
    4. 범위

[문제해결과정]
1. 입력값 받고
2. N개의 정수를 리스트에 넣어주고
3. 산술 평균 : sum()한 값을 N으로 나눠주기, round()로 반올림
4. 중앙값: 인덱스 슬라이싱
5. 최빈값 : for문? Counter?
6. 범위 : max() - min()
7. 각각 출력
'''
#코드
import sys
import statistics
from collections import Counter


input = sys.stdin.readline

nums = []
result = []

N = int(input())

for _ in range(N):
    num = int(input())
    nums.append(num)

nums.sort()

#산술평균
print(round(sum(nums) / N))
#중앙값
print(nums[N // 2])
#최빈값
temp = Counter(nums).most_common()
if len(temp) > 1 and temp[0][1] == temp[1][1]:
    print(temp[1][0])
else:
    print(temp[0][0])
#범위
print(max(nums) - min(nums))